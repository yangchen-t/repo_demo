package main

import (
	"fmt"
	"sort"
)

type PathInfo struct {
	Path  string `yaml:"path"`
	Level int    `yaml:"level"`
}

// Configuration 结构体定义
type Configuration struct {
	Standard    int                 `yaml:"standard"`
	TriggerTime int                 `yaml:"trigger_time"`
	Day         int                 `yaml:"day"`
	Pathlist    map[string]PathInfo `yaml:"pathlist"`
}

func main() {
	// 示例 Configuration 结构体
	config := Configuration{
		Standard:    1,
		TriggerTime: 5,
		Day:         3,
		Pathlist: map[string]PathInfo{
			"path1": {Path: "/path1", Level: 3},
			"path2": {Path: "/path2", Level: 5},
			"path3": {Path: "/path3", Level: 2},
		},
	}

	// 定义排序函数
	sortedKeys := make([]string, 0, len(config.Pathlist))
	for key := range config.Pathlist {
		sortedKeys = append(sortedKeys, key)
	}
	sort.Slice(sortedKeys, func(i, j int) bool {
		return config.Pathlist[sortedKeys[i]].Level < config.Pathlist[sortedKeys[j]].Level
	})

	// 输出排序后的结果
	for _, key := range sortedKeys {
		fmt.Printf("Key: %s, Path: %s, Level: %d\n", key, config.Pathlist[key].Path, config.Pathlist[key].Level)
	}
}
