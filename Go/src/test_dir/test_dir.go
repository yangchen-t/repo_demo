package test_dir

import (
	"fmt"
)

type Str string 

const (
	Str_test Str = "stringtype"
)

type Person struct {
    Name  string  `json:"name"`
    Age     int   `json:"age"`
    Email string  `json:"email"`
}



func Print_test(){
	fmt.Println("this is frist test msg")
}
func Test_pkg() {
	fmt.Println("测试包的导入")
}
