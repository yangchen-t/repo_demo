package main

import (
	"bytes"
	"fmt"
	"os/exec"
	"strings"
	"time"
)

// func received(c chan int) {
// 	// for {
// 	// 	v, ok := <-c
// 	// 	fmt.Printf("v = %d, ok = %t\n",v,ok)
// 	// 	time.Sleep(time.Second)
// 	// 	if !ok {
// 	// 		fmt.Println("close")
// 	// 		break
// 	// 	}
// 	for v := range c {
// 		fmt.Printf("v = %d\n", v)
// 		time.Sleep(time.Second)
// 	}

// }

func runCmd(cmdStr string) string {
	// var s_array []string
	list := strings.Split(cmdStr, " ")
	cmd := exec.Command(list[0], list[1:]...)
	var out bytes.Buffer
	var stderr bytes.Buffer
	cmd.Stdout = &out
	cmd.Stderr = &stderr
	err := cmd.Run()
	if err != nil {
		return stderr.String()
	} else {
		return out.String()
	}
}

func main() {
	// a := make(chan int, 200)
	for i := 0; i < 5; i++ {
		a <- runCmd("date")
	}
	close(a)
	time.Sleep(time.Second)
	for j := 0; j < 3; j++ {
		e, ok := <-a
		fmt.Printf("e = %d,ok = %t\n", e, ok)
		if !ok {
			fmt.Printf("close\n")
			break
		}
	}
}

// 		// a <- 1011
// 		// close(a)
// 		// received(a)
// }

// func main() {
// 	ch := make(chan int, 1) //创建一个类型为int，缓冲区大小为1的通道
// 	for i := 1; i <= 10; i++ {
// 		select {
// 		case x := <-ch: //第一次循环由于没有值，所以该分支不满足
// 			fmt.Println(x)
// 		case ch <- i: //将i发送给通道(由于缓冲区大小为1，缓冲区已满，第二次不会走该分支)
// 			fmt.Println("jump")
// 		}
// 	}
// }
