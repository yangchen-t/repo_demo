package main

import (
	"fmt"
	"golang.org/x/net/websocket"
	"log"
	"net/http"
)
func Echo(ws *websocket.Conn) {
	// websocket.Conn  用来作为客户端和服务器端交互的通道
	var err error
	// 只是用来记录接收请求的次数
    var i int
	for {
		var reply string
		// 建立连接后 接收来自客户端的信息reply
		if err = websocket.Message.Receive(ws, &reply); err != nil {
			fmt.Println("Error! Can't receive message...")
			break
		}
		fmt.Println("Received from client: " + reply)
        i++
        // 把收到的信息进行处理,也可以做信息过滤,也可以返回固定的信息
		msg := "Received:  " + reply
		fmt.Println("Sending to client: " + msg)
        fmt.Println(i)
		// 把信息返回发送给客户端 
		if err = websocket.Message.Send(ws, msg); err != nil {
			fmt.Println("Error! Can't send message...")
			break
		}
	}
}

func main() {
	http.Handle("/", websocket.Handler(Echo))


	if err := http.ListenAndServe(":8888", nil); err != nil {
		log.Fatal("ListenAndServe:", err)
	}   // 访问服务器的地址,ip没有限制,端口是8888,
	   //  ws://127.0.0.1:8888 
}

