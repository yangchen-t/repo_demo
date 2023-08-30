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
const IsEmpty string = ""

type VersionCompare struct {
	CompareResult  map[string]string
	DisconnectList map[string]string
	VersionList    map[string]string
}
type ConnectInfo struct {
	VehicleList []string      `yaml:"vehiclelist"`
	Port        int           `yaml:"port"`
	Protocol    string        `yaml:"protocol"`
	Hostname    string        `yaml:"hostname"`
	Passwd      string        `yaml:"passwd"`
	Command     string        `yaml:"command"`
	Timeout     time.Duration `yaml:"timeout"`
}

var Version VersionCompare
var data ConnectInfo

var Sync struct {
	wg sync.WaitGroup
	mu sync.Mutex
}

func GetVersionInfo(VehIp string, info ConnectInfo, done func()) {
	defer done()
	// 建立SSH客户端连接
	client, err := ssh.Dial(info.Protocol, string(VehIp+":"+strconv.Itoa(info.Port)), &ssh.ClientConfig{
		User:            info.Hostname,
		Auth:            []ssh.AuthMethod{ssh.Password(info.Passwd)},
		HostKeyCallback: ssh.InsecureIgnoreHostKey(),
		Timeout:         time.Second * info.Timeout,
	})

	if err != nil {
		if os.Getenv("Vdebug") == "1" {
			fmt.Println(err)
		}
		Sync.mu.Lock()
		Version.CompareResult[VehIp] = IsEmpty
		Sync.mu.Unlock()
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
	Version.CompareResult[VehIp] = string(result)
}

func ConnectDevices(info ConnectInfo) {
	Sync.wg.Add(len(info.VehicleList))
	Version.CompareResult = make(map[string]string, len(info.VehicleList))
	for i := 0; i < len(info.VehicleList); i++ {
		go GetVersionInfo(info.VehicleList[i], info, Sync.wg.Done)
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
	fmt.Printf("当前较多的版本为: %s\n", maxValue)
	return maxValue
}

func CompareDiffVersion() {
	Version.VersionList = make(map[string]string, len(Version.CompareResult))
	Version.DisconnectList = make(map[string]string, len(Version.CompareResult))
	for k, v := range Version.CompareResult {
		if v == IsEmpty {
			Version.DisconnectList[k] = "offline"
		} else {
			Version.VersionList[k] = v
		}
	}
	fmt.Println("-------------设备不在线列表-------------")
	for VehicleId, Offline := range Version.DisconnectList {
		fmt.Printf("%-20s %s\n", VehicleId, Offline)
	}
	fmt.Println("----------------结束线-----------------")
	fmt.Println("----------------版本对比---------------")
	CurVersion := StatisticalAlgorithms(Version.VersionList)
	for Ck, Cv := range Version.VersionList {
		if Cv != CurVersion {
			fmt.Printf("%s 版本存在差异\n%s 的当前版本为%s", Ck, Ck, Cv)
		}
	}
	fmt.Println("----------------结束线-----------------")
}

// 5s over
func main() {
	ReadConf()
	Sync.wg.Wait()
	CompareDiffVersion()
}
