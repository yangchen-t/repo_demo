package main

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
	"sort"
	"syscall"
)

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

func main() {

}
