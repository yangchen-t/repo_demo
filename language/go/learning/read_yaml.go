package main

import (
	"fmt"

	"github.com/spf13/viper"
)

func main() {
	// 设置配置文件的名字
	v := viper.New()
	v.AddConfigPath(".")
	v.SetConfigName("90-monitor")
	// 设置配置文件的类型
	v.SetConfigType("yaml")
	// 添加配置文件的路径，指定 config 目录下寻找

	// 寻找配置文件并读取
	err := v.ReadInConfig()
	if err != nil {
		panic(fmt.Errorf("fatal error config file: %w", err))
	}
	fmt.Println(v.Get("Monitor"))                         // map[port:3306 url:127.0.0.1]
	fmt.Println(v.Get("Monitor.Disk.DefaultSysdiskSize")) // 127.0.0.1
	// v2 := v.Sub("mysql")
	// fmt.Println(v2.GetString("port"))
}
