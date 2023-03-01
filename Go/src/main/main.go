package main

import (
	"fmt"
	"src/test_dir"
)

// func print(p1 *Person){
// 	fmt.Println("name = %d, Age = %d, Email = %d\n", p1.Name,p1,Age,p1.Email)
// }	


func main(){
	test_dir.Test_pkg()

	p1 := test_dir.Person{
		Name: "test",
		Age: 10,
		Email: "xxx@xx",
	}

	// var p1 *test_dir.Person
	// print(&p1)
	fmt.Printf("name = %s, Age = %d, Email = %s\n", p1.Name,p1.Age,p1.Email)
	fmt.Println("const str = ", test_dir.Str_test)
}
