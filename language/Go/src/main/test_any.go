
package main

import (
	"fmt"
	"os"
	"os/exec"
	"regexp"
	"strings"
	"time"
	"github.com/godbus/dbus/v5"
)

func eventPtpListen(writer func(eventStr string, a any)) {
	type output struct {
		out []byte
		err error
	}

	for {

		ch := make(chan output)

		go func() {
			// cmd := exec.Command("false")
			for {

				cmd := exec.Command("systemctl", "status", "qomolo_gateway_sys2phc.service")
				out, err := cmd.CombinedOutput()
				ch <- output{out, err}
			}
		}()

		select {
		case <-time.After(2 * time.Second):
			fmt.Println("timed out")
		case x := <-ch:
			if x.err == nil {
				if matched, err := regexp.MatchString("Active: active", string(x.out)); err == nil && matched {
					xx := strings.Split(string(x.out), "\n")
					xx = delete_empty(xx)

					writer("sys2phc", Message{
						Name:   "sys2phc",
						Status: xx[len(xx)-1],
					})
				}
				if x.err != nil {
					fmt.Printf("program errored: %s\n", x.err)
				}
			}
		}

		// inputCmd := "systemctl state qomolo_gateway_sys2phc.service"
		// stdout, err := exec.Command("bash", "-c", inputCmd).Output()
		// fmt.Println(err)
		// fmt.Println(string(output))
		// }
		time.Sleep(1 * time.Second)
	}

}