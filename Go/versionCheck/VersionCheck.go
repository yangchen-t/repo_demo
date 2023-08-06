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
var mu sync.Mutex
var CompareResult map[string]string
var IsEmpty string = ""
var DisconnectList map[string]string
var VersionList map[string]string

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
		fmt.Println(err)
		mu.Lock()
		CompareResult[VehIp] = IsEmpty
		mu.Unlock()
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

func StatisticalAlgorithms(VersionList map[string]string) string {
	// 创建一个用于存储出现次数的 map
	counts := make(map[string]int)

	// 统计 values 出现的次数
	for _, value := range VersionList {
		counts[value]++
	}

	// 找出出现次数最多的 value
	maxCount := 0
	maxValue := ""
	for value, count := range counts {
		if count > maxCount {
			maxCount = count
			maxValue = value
		}
	}
	// 打印出现最多的 value 和其出现次数
	fmt.Printf("出现最多的 value 是 %s，出现了 %d 次。\n", maxValue, maxCount)
	return maxValue
}

func CompareDiffVersion() {
	VersionList = make(map[string]string, len(CompareResult))
	DisconnectList = make(map[string]string, len(CompareResult))
	for k, v := range CompareResult {
		if v == IsEmpty {
			DisconnectList[k] = "offline"
		} else {
			VersionList[k] = v
		}
	}
	fmt.Println("-----Disconnect Vehicle List ------")
	for VehicleId, Offline := range DisconnectList {
		fmt.Printf("%-20s %s\n", VehicleId, Offline)
	}
	fmt.Println("---------------结束线---------------")
	fmt.Println("-------Check Vehicle List --------")
	fmt.Println(VersionList)
	CurVersion := StatisticalAlgorithms(VersionList)
	for Ck, Cv := range VersionList {
		if Cv != CurVersion {
			fmt.Println(Ck, "版本存在差异, 标准为：", CurVersion, "当前为: ", Cv)
		}
	}
}

// 5s over
func main() {
	ReadConf()
	wg.Wait()
	CompareDiffVersion()
}
