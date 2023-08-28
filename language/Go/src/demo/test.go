package main 

import "fmt"

func add_var()int{
	var s [] int 
	s = append(s,0)
	number := cap(s)
	return number
}

func init(){
	fmt.Println("int func")
}

func main(){
	array := [5]int{1,2,3,4,5}
	var spilt []int = array[1:3]
	var x int 
	x = 9
	spilt[1]= x 
	fmt.Println(spilt)
	fmt.Println(array)  
	add_var()
}