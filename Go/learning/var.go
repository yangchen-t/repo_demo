package main

import "fmt"

func main() {
	// 声明格式 var 变量名 类型  ， 声明必用
	var a int
	fmt.Println("a = ", a) //  一段一段处理，自动加换行
	a = 10
	fmt.Println("a = ", a)

	// var a int = 10 // 初始化赋值
	// a = 20         // 赋值

	// 自动推导类型， 必须初始化，根据初始化的值确定类型
	c := 30
	// %T 打印变量所属的类型
	fmt.Printf("c type is %T\n", c) // 格式化传输      \n 自动换行

	// 变量声明关键字     var
	// 常量声明关键字     const
	const b = 10 // const 不能使用 :=
	fmt.Printf("b = %T\n", b)
	const (
		i = 1
		s = 3.14
	)
	fmt.Println("i = ", i)
	fmt.Println("s = ", s)

}
