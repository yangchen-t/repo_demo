package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"sort"
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

var creationTime = make(map[string]int)
var v []PathInfo
var multiMap = make(map[int]string)

// const CONFIG = "config.yaml"

func sortMapByValue(m map[string]int) map[string]int {
	keys := make([]string, 0, len(m))

	for key := range m {
		keys = append(keys, key)
	}

	sort.Slice(keys, func(i, j int) bool {
		return m[keys[i]] < m[keys[j]] // 降序排列
	})

	return m
}

func getCreateTime(filepath string) map[string]int {
	info, err := os.Stat(filepath)

	if err == nil {
		cTime := int(info.ModTime().Unix())
		creationTime[filepath] = cTime
	} else {
		fmt.Println("Stat error for:", filepath)
	}
	return creationTime
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

func timeTransform(day int) int {
	currentTime := time.Now().Unix()
	return int(currentTime - int64(day*24*60*60))
}

// Implement other functions and main function translation here
func findPath(directory string) {
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
			if info.IsDir() {
				findPath(path)
			}
			return nil
		})
	if err != nil {
		log.Println(err)
	}
}

func currentFreeSpace() int {
	var stat syscall.Statfs_t
	err := syscall.Statfs("/", &stat)
	if err == nil {
		return int(stat.Bavail * uint64(stat.Bsize) / (1 << 30))
	}
	return -1
}

// func convert() {
// 	for key, value := range creationTime {
// 		multiMap[value] = key
// 	}
// }

// func autoClean(threshold int, day int) {
// 	sort.Slice(v, func(i, j int) bool {
// 		return v[i].Size < v[j].Size
// 	})

// 	for _, info := range v {
// 		fmt.Println(directorySizeCount(info.Path))
// 		if directorySizeCount(info.Path) > info.Size {
// 			fmt.Printf("Directory %s exceeds size limit\n", info.Path)
// 			files := make([]PathInfo, 0)

// 			err := filepath.Walk(info.Path, func(path string, file os.FileInfo, err error) error {
// 				if err != nil {
// 					return err
// 				}
// 				if !file.IsDir() && !isSpecialFileType(path) {
// 					files = append(files, PathInfo{
// 						Path:  path,
// 						Name:  file.Name(),
// 						Size:  float64(file.Size()) / (1 << 30),
// 						Level: info.Level,
// 					})
// 				}
// 				return nil
// 			})

// 			if err != nil {
// 				fmt.Println("Error walking through directory:", err)
// 			}

// 			sort.Slice(files, func(i, j int) bool {
// 				return files[i].Size < files[j].Size
// 			})

// 			clearedSize := 0.0
// 			for _, file := range files {
// 				if clearedSize+file.Size < info.Size {
// 					fmt.Printf("Deleting file %s\n", file.Path)
// 					err := os.Remove(file.Path)
// 					if err != nil {
// 						fmt.Println("Error deleting file:", err)
// 					} else {
// 						clearedSize += file.Size
// 					}
// 				}
// 			}

// 			if clearedSize >= info.Size {
// 				fmt.Printf("Directory %s cleaned successfully\n", info.Path)
// 			} else {
// 				fmt.Printf("Not enough space freed in directory %s\n", info.Path)
// 			}
// 		}
// 	}
// }

// Implement other functions and main function translation here

func main() {
	// for {
	// 读取配置文件
	configFile, err := ioutil.ReadFile("config.yaml")
	if err != nil {
		fmt.Println("Error reading config file:", err)
		return
	}

	var config map[string]interface{}
	err = yaml.Unmarshal(configFile, &config)
	if err != nil {
		fmt.Println("Error parsing YAML config:", err)
		return
	}

	// 获取 pathlist 字段
	pathList, ok := config["pathlist"].(map[interface{}]interface{})
	if !ok {
		fmt.Println("Invalid or missing 'pathlist' field in the configuration")
		return
	}

	// 遍历并输出每个路径信息
	for key, value := range pathList {
		pathInfo, ok := value.(map[interface{}]interface{})
		if !ok {
			fmt.Printf("Invalid format for %s path info\n", key)
			continue
		}

		path := pathInfo["path"].(string)
		fmt.Println("--->", path)
		findPath(path)
		fmt.Println(directorySizeCount(path))
	}
	for key, value := range sortMapByValue(creationTime) {
		fmt.Println(key, " ==> ", value)
	}
	time.Sleep(1 * time.Second)

	// }
}
