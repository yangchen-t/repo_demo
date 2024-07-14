package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"sort"
	"sync"
	"syscall"
	"time"

	"gopkg.in/yaml.v2"
)

// Level represents the priority level of a PathInfo
type Level int

const (
	Low Level = iota
	Middle
	High
)

// PathInfo contains information about a directory path
type PathInfo struct {
	Path  string
	Name  string
	Size  float64
	Level Level
}

type Configuration struct {
	Standard    int                 `yaml:"standard"`
	TriggerTime int                 `yaml:"trigger_time"`
	Day         int                 `yaml:"day"`
	Pathlist    map[string]PathInfo `yaml:"pathlist"`
}

var creationTime = make(map[string]int)
var creationTimeSort = make(map[string]int)
var mutex sync.Mutex

const monitorMountdPoint string = "/data"

func timeTransform(day int) int {
	currentTime := time.Now().Unix()
	return int(currentTime - int64(day*24*60*60))
}

func currentFreeSpace() int {
	var stat syscall.Statfs_t
	err := syscall.Statfs(monitorMountdPoint, &stat)
	if err == nil {
		return int(stat.Bavail * uint64(stat.Bsize) / (1 << 30))
	}
	return -1
}
func isSpecialFileType(filePath string) bool {
	// Define conditions to check for special file types here
	return filePath[0] == '.' // Example: Check if file name starts with '.'
}
func directorySizeCount(folderPath string) float64 {
	var size int64

	err := filepath.Walk(folderPath, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if !info.IsDir() && !isSpecialFileType(path) {
			size += info.Size()
		}
		return nil
	})

	if err != nil {
		fmt.Println("Error calculating directory size:", err)
	}

	sizeGB := float64(size) / (1 << 30) // Convert to GB
	return sizeGB
}
func getCreateTime(filepath string) {
	info, err := os.Stat(filepath)

	if err == nil {
		cTime := int(info.ModTime().Unix())
		creationTime[filepath] = cTime
	} else {
		fmt.Println("Stat error for:", filepath)
	}
}

func findPath(directory string) {
	mutex.Lock()
	defer mutex.Unlock()
	err := filepath.Walk(directory,
		func(path string, info os.FileInfo, err error) error {
			if err != nil {
				return err
			}
			baseName := filepath.Base(path)
			if baseName != "" && baseName[0] == '.' {
				if info.IsDir() {
					return filepath.SkipDir // 忽略以 . 开头的文件夹
				}
				return nil // 忽略以 . 开头的文件
			}
			if !info.IsDir() {
				getCreateTime(path) // 获取文件的创建时间
			}
			return nil
		})
	if err != nil {
		log.Println(err)
	}
}

func mySort() {
	// 将 map 转换为切片以便排序
	var sortedTimes []string
	for key := range creationTime {
		sortedTimes = append(sortedTimes, key)
	}

	sort.Slice(sortedTimes, func(i, j int) bool {
		return creationTime[sortedTimes[i]] < creationTime[sortedTimes[j]]
	})
	for _, key := range sortedTimes {
		if val, ok := creationTime[key]; ok {
			creationTimeSort[key] = val
		}
	}
}

func removeFileReleaseSpaceByDay(standardTimeStamp int, Standard int) {
	for key, value := range creationTime {
		if value <= standardTimeStamp {
			if currentFreeSpace() < Standard {
				if _, err := os.Stat(key); err == nil {
					fmt.Println(currentFreeSpace(), "->", Standard, "t -> ", key, " [", value, " -> ", standardTimeStamp, "]")
					_ = os.Remove(key)
				} else if os.IsNotExist(err) {
					fmt.Println("File does not exist.")
				} else {
					fmt.Println("Error checking file existence:", err)
				}
			} else {
				return
			}
		} else {
			fmt.Println(directorySizeCount(key))
			return
		}
	}
}
func removeFileReleaseSpaceBySize(Standard int, p PathInfo) {
	// 将 creationTime 按照创建时间升序排序
	var sortedKeys []string
	for key := range creationTime {
		sortedKeys = append(sortedKeys, key)
	}
	sort.Slice(sortedKeys, func(i, j int) bool {
		return creationTime[sortedKeys[i]] < creationTime[sortedKeys[j]]
	})

	for _, key := range sortedKeys {
		if directorySizeCount(p.Path) > p.Size {
			if currentFreeSpace() < Standard {
				if _, err := os.Stat(key); err == nil {
					fmt.Println(currentFreeSpace(), "->", Standard, "s -> ", key)
					_ = os.Remove(key)
					delete(creationTime, key) // 删除已处理的文件
				} else if os.IsNotExist(err) {
					fmt.Println("File does not exist.")
				} else {
					fmt.Println("Error checking file existence:", err)
				}
			} else {
				return
			}
		} else {
			fmt.Println(directorySizeCount(p.Path), "S==>", p.Size)
			return
		}
	}
}
func autoClean(c Configuration, sort []string) {
	// 遍历并输出每个路径信息
	for _, key := range sort {
		// fmt.Println(c.Pathlist[key].Path)
		findPath(c.Pathlist[key].Path)
		removeFileReleaseSpaceByDay(timeTransform(c.Day), c.Standard)
	}
	if currentFreeSpace() > c.Standard {
		return
	} else {
		for _, key := range sort {
			// fmt.Println(c.Pathlist[key].Path)
			findPath(c.Pathlist[key].Path)
			mySort()
			removeFileReleaseSpaceBySize(c.Standard, c.Pathlist[key])
		}
	}

}

func main() {
	for {
		// 读取 YAML 配置文件
		yamlFile, err := ioutil.ReadFile("/opt/qomolo/utils/qpilot_setup/service_scripts/config.yaml")
		if err != nil {
			fmt.Println("Error reading YAML file:", err)
			return
		}

		// 解析 YAML 数据到 Configuration 结构
		var config Configuration
		err = yaml.Unmarshal(yamlFile, &config)
		if err != nil {
			fmt.Println("Error parsing YAML data:", err)
			return
		}
		time.Sleep(time.Duration(config.TriggerTime) * time.Second)

		// 定义排序函数
		sortedKeys := make([]string, 0, len(config.Pathlist))
		for key := range config.Pathlist {
			sortedKeys = append(sortedKeys, key)
		}
		sort.Slice(sortedKeys, func(i, j int) bool {
			return config.Pathlist[sortedKeys[i]].Level < config.Pathlist[sortedKeys[j]].Level
		})
		if currentFreeSpace() < config.Standard {
			autoClean(config, sortedKeys)
		}
	}
}
