package main

import "fmt"

func main() {

	// iota 常量自动生成器，每行自动加+
	// iota 给常量赋值使用
	const (
		a = iota
		b = iota
		c = iota
	)
	fmt.Printf("a = %d, b = %d, c = %d\n", a, b, c)

	// iota 遇到const，重置为0
	const d = iota
	fmt.Printf("d = %d\n", d)

	// 如果同一行，值都是一样的
	const (
		a1     = iota
		b1, b2 = iota, iota
	)
	fmt.Printf("a1 = %d, b1 = %d, b2 = %d\n", a1, b1, b2)
}
