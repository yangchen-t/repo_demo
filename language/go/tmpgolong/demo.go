package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"

	"gopkg.in/yaml.v2"
)

// const fileName string = "test.conf"
const PROFILE string = "wuhuan.yaml"

// const HEADCONFIG string = `[inet_http_server]
// chmod=0777
// chown=nobody:nogroup
// port=0.0.0.0:9001
// username=qomolo
// password=123

// [supervisord]
// nodaemon=true
// `

type element struct {
	Scripts     string `json:"scripts"`
	Output      string `json:"output"`
	Autostart   bool   `json:"autostart"`
	Autorestart bool   `json:"autorestart"`
}

type conf struct {
	Name map[string]element `yaml:"name"`
}

type profile struct {
	Profile map[string]conf `json:"profile"`
}

// type CurModule struct {
// 	Cur  map[string]bool `map:"cur"`
// 	Base map[string]bool `map:"Base"`
// }

// var moduleStats CurModule

// func WriteFile(str string) {
// 	f, err := os.Create(fileName)
// 	if err != nil {
// 		fmt.Println(err.Error())
// 	} else {
// 		_, err = f.WriteString(str)
// 	}
// 	defer f.Close()
// }

// func AddFileContent(str string) {
// 	file, err := os.OpenFile(fileName, os.O_WRONLY|os.O_APPEND, 0666)
// 	if err != nil {
// 		fmt.Println("文件打开失败", err)
// 	}
// 	defer file.Close()
// 	//写入文件时，使用带缓存的 *Writer
// 	write := bufio.NewWriter(file)
// 	write.WriteString("\n")
// 	write.WriteString(str)
// 	//Flush将缓存的文件真正写入到文件中
// 	write.Flush()
// }

// func WriteFileModule(moduleNaeme, startScripts, output, autostart, autorestart string) {
// 	str := `[program:%s]
// command=/scripts/%s
// stdout_logfile=/debug/%s
// stdout_logfile_maxbytes=10MB
// stdout_logfile_backups=50
// redirect_stderr=true
// autostart=%s
// autorestart=%s
// startretries=5
// stopasgroup=true
// stopsignal=INT
// priority=999
// `
// 	AddFileContent(fmt.Sprintf(str, moduleNaeme, startScripts, output, autostart, autorestart))
// }

func readConf() {
	_, err := os.Stat(PROFILE)
	if os.IsNotExist(err) {
		fmt.Println("file is not exist: ", PROFILE)
		os.Exit(-1)
	}
	file, err := ioutil.ReadFile(PROFILE)
	if err != nil {
		log.Fatal(err)
	}
	var data []profile
	err2 := yaml.Unmarshal(file, &data)

	if err2 != nil {
		log.Fatal(err2)
	}

	for _, v := range data {
		fmt.Println(v)
	}

	// moduleStats.Base = make(map[string]bool)
	// for _, v := range data {
	// 	// TODO 这里需要提供一个变量区分项目. 或者传入一个变量均可
	// 	if v.Project == "wh" {
	// 		// TODO 这里需要环境变量区分不同的dcu， 或者切割entrypoint_105模块取得，或者传入变量
	// 		if os.Getenv("device_type") == "105" {
	// 			for _, m := range v.Dcu1 {
	// 				for name, stats := range m {
	// 					moduleStats.Base[name] = stats
	// 				}

	// 			}
	// 		} else {
	// 			for _, m := range v.Dcu2 {
	// 				for name, stats := range m {
	// 					moduleStats.Base[name] = stats
	// 				}
	// 			}
	// 		}
	// 	}
	// }
}

func main() {
	// WriteFile(HEADCONFIG)
	readConf()
	// for name, _ := range moduleStats.Base {
	// 	WriteFileModule(name, "%(program_name)s.sh", "%(program_name)s.log", "false", "false")
	// }

}
