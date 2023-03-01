package main 

import (
	"fmt"
)

type Service interface {
    Start()  // 开启服务
    Log(string)  // 日志输出
	PrintLogger()
}

// 日志器
type Logger struct {
	str string 
}
// 实现Service的Log()方法
func (g *Logger) Log(s string){
	fmt.Println("print = ", Logger{str: s})

}

type GameService struct {
    Logger  // 嵌入日志器
}
// 实现Service的Start()方法
func (g *GameService) Start(){
	fmt.Println("start")
}

func main(){
	var	a Service = new(GameService)
	a.Start()
	a.Log("interface call")
	a.PrintLogger()



}