package main

import (
	"fmt"

	"github.com/cierdes/supervisor-api/supervisor"
)

// func main() {
// 	client, err := supervisor.NewSupervisor("qomolo:123@192.168.13.105:9001")
// 	if err != nil {
// 		fmt.Println(err)
// 		return
// 	}
// 	defer client.Close()

// 	r, err := client.ListMethods()
// 	if err != nil {
// 		fmt.Println(err)
// 		return
// 	}
// 	// var NameList []string

// 	fmt.Println(r)
// 	ret, _ := client.GetAllProcessInfo()
// 	fmt.Println(len(ret))
// 	for i := 0; i < len(ret); i++ {
// 		fmt.Println(ret[i].ProcessName)
// 	}
// 	// fmt.Println(NameList)
// 	// tail log
// }

// func main() {
// 	// url := "http://localhost:9001/RPC2"
// 	events := make(chan interface{})
// 	// mon, err := supervisor.NewMonitor(url, os.Stdin, os.Stdout, events)
// 	client, err := sapi.NewSupervisor("http://qomolo:123@192.168.103.105:9001", os.Stdin, os.Stdout, events)
// 	if err != nil {
// 		fmt.Fprintf(os.Stderr, "Error: %s\n", err)
// 		os.Exit(1)
// 	}

// 	done := make(chan bool)
// 	go func() {
// 		for event := range events {
// 			switch event.(type) {
// 			case sapi.ProcessAddEvent:
// 				process := (event.(sapi.ProcessAddEvent)).Process
// 				fmt.Fprintf(os.Stderr, "Process %s added\n", process.Name)
// 			case sapi.ProcessRemoveEvent:
// 				process := (event.(sapi.ProcessRemoveEvent)).Process
// 				fmt.Fprintf(os.Stderr, "Process %s added\n", process.Name)
// 			case sapi.ProcessStateEvent:
// 				process := (event.(sapi.ProcessStateEvent)).Process
// 				from := (event.(sapi.ProcessStateEvent)).FromState
// 				fmt.Fprintf(os.Stderr, "Process %s state change %s => %s\n", process.Name, from, process.State)
// 			case sapi.SupervisorStateEvent:
// 				sapi := (event.(sapi.SupervisorStateEvent)).Supervisor
// 				from := (event.(sapi.SupervisorStateEvent)).FromState
// 				fmt.Fprintf(os.Stderr, "sapi \"%s\" state change %s => %s\n", sapi.Name, from, sapi.State)
// 			default:
// 				fmt.Fprintf(os.Stderr, "Unchecked Event: %+v\n", event)
// 			}
// 		}
// 		done <- true
// 	}()

// 	mon.Refresh()
// 	mon.Run()

// 	close(events)
// 	mon.Close()
// 	<-done
// }

var my []string

func test01() {

	client, err := supervisor.NewSupervisor("qomolo:123@192.168.103.105:9001")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer client.Close()
	ret, _ := client.GetAllProcessInfo()
	for i := 0; i < len(ret); i++ {
		my = append(my, ret[i].ProcessName)
	}
	fmt.Println(my)
}

func testmap() {
	// mymap := make(map[string]string, 10)
	mymap := map[string]string{
		"test01": "1",
		"test02": "2",
	}
	mymap = map[string]string{
		"test03": "1",
		"test04": "2",
	}

	fmt.Println(mymap)
}

func main() {
	test01()
	testmap()
}
