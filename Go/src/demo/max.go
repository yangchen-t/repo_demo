package main 

import "fmt"

func max(a, b int)int{
	if a > b {
		return a 
	}
	return b 
}

func main(){
// 	a, b := 100, 20
// 	ret := max(a, b) 
// 	fmt.Println(ret)
	// var array = []float64{10.0,2.3,123}
	// array[2] = 30
	// myarray := array
	// fmt.Println(myarray[1])
	// var a = [2][7]int{ {0,0,2,3}, {1,2,2,4,3,6}}
	// fmt.Println(a[1][3])

	// var number = make([]int ,10,10)
	// fmt.Printf("number len = %d, cap = %d\n", len(number),cap(number))
	// number[0] = 10
	// fmt.Println(number)

	array := []int{10,1,2,3,4,5} 
	for _,b := range array{                
		fmt.Printf("b = %d \n",b)
	}


}