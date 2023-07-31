package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"strconv"
	"sync"
	"time"

	"golang.org/x/crypto/ssh"
	"gopkg.in/yaml.v2"
)

const PROFILE string = "conf.yaml"
const timeout time.Duration = time.Second * 5

var wg sync.WaitGroup
var CompareResult map[string]string

type ConnectInfo struct {
	VehicleList []string `yaml:"vehiclelist"`
	Port        int      `yaml:"port"`
	Protocol    string   `yaml:"protocol"`
	Hostname    string   `yaml:"hostname"`
	Passwd      string   `yaml:"passwd"`
	Command     string   `yaml:"command"`
}

func GetVersionInfo(VehIp string, info ConnectInfo, done func()) {
	// fmt.Println("===========", VehIp, "===========")
	defer done()
	// 建立SSH客户端连接
	client, err := ssh.Dial(info.Protocol, string(VehIp+":"+strconv.Itoa(info.Port)), &ssh.ClientConfig{
		User:            info.Hostname,
		Auth:            []ssh.AuthMethod{ssh.Password(info.Passwd)},
		HostKeyCallback: ssh.InsecureIgnoreHostKey(),
		Timeout:         timeout,
	})
	if err != nil {
		fmt.Println("SSH dial error:", err.Error())
		return
	}

	// 建立新会话
	session, err := client.NewSession()
	defer session.Close()

	if err != nil {
		log.Fatalf("new session error: %s", err.Error())
	}

	result, err := session.Output(info.Command)
	if err != nil {
		fmt.Fprintf(os.Stdout, "Failed to run command, Err:%s", err.Error())
		os.Exit(0)
	}
	CompareResult[VehIp] = string(result)
}

func ConnectDevices(info ConnectInfo) {
	wg.Add(len(info.VehicleList))
	CompareResult = make(map[string]string, len(info.VehicleList))
	for i := 0; i < len(info.VehicleList); i++ {
		go GetVersionInfo(info.VehicleList[i], info, wg.Done)
	}
}

func ReadConf() {
	_, err := os.Stat(PROFILE)
	if os.IsNotExist(err) {
		fmt.Println("file is not exist: ", PROFILE)
		os.Exit(-1)
	}
	file, err := ioutil.ReadFile(PROFILE)
	if err != nil {
		log.Fatal(err)
	}
	var data ConnectInfo
	err2 := yaml.Unmarshal(file, &data)

	if err2 != nil {
		log.Fatal(err2)
	}
	ConnectDevices(data)
}

func CompareDiffVersion() {
	fmt.Println(CompareResult)
}

// 5s over
func main() {
	ReadConf()
	wg.Wait()
	CompareDiffVersion()
}
