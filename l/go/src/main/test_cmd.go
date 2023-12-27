package main

import (
    "strings"
    "bytes"
    "os/exec"
    "fmt"
)


func runCmd(cmdStr string) string{
	type output struct{
		err error
		out []string
	}
	// ch := make(chan string)
    list := strings.Split(cmdStr, " ")
    fmt.Println(list)
    cmd := exec.Command(list[0],list[1:]...)
	fmt.Println(cmd)
    var( 
		out bytes.Buffer
    	stderr bytes.Buffer
	)
	cmd.Stdout = &out
    cmd.Stderr = &stderr
    err := cmd.Run()
    if err != nil {
        return stderr.String()
    } else {
        return out.String()
    }
}

func main(){
    // var s string =  `| sort -rnk 9  | head -n 10`
    ret := runCmd("pidstat -r 1 1")
	fmt.Println(ret)
    // for _, ret := range ret {
    //     fmt.Printf("ret=%c\n", ret)
    // }
    str1 := []string{"hello", "world", "hello", "golang"}
    res20 := strings.Join(str1, "+")
    fmt.Printf("res20 is %v\n", res20)
}


