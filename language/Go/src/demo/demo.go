package main

import (
	"fmt"

	// "gitlab.qomolo.com/infrastructure/sw_architecture/management_plane/management_plane/model"
	// "gitlab.qomolo.com/infrastructure/sw_architecture/management_plane/management_plane/pkg/controller"
)


type Person struct {
    Name  string  `json:"name"`
    Age     int   `json:"age"`
    Email string  `json:"email"`
}


func main(){
	var p1 *Person
	p1 := &Person{
		Name : "nick",
		Age : 2
		Email : "xxxx@xxxx"
	}
	fmt.Printf("name = %s, Age = %d, Email = %s\n", p1.Name,p1.Age,p1.Email)
}





// func runCmd(cmdStr string) string {
// 	// var s_array []string
// 	list := strings.Split(cmdStr, " ")
// 	cmd := exec.Command(list[0], list[1:]...)
// 	var out bytes.Buffer
// 	var stderr bytes.Buffer
// 	cmd.Stdout = &out
// 	cmd.Stderr = &stderr
// 	err := cmd.Run()
// 	if err != nil {
// 		return stderr.String()
// 	} else {
// 		return out.String()
// 	}
// }