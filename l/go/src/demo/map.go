package main 

import "fmt"

func main(){

	mymap := make(map[int]string)
	mymap[1] = "a"
	mymap[2] = "b"
	mymap[3] = "c"

	for i,_ := range mymap{
		fmt.Println("i = ", i , "mymap_key = " ,mymap[i])
		if i == 1 || i == 3{
			// fmt.Printf("i = %d, str = %s\n",i,str)
			fmt.Printf("start del \n")
			delete(mymap, i)
		}
	}
	fmt.Printf("------------\n")
	for i, _:= range mymap{
		fmt.Println("i = ", i ,"str = ", mymap[i])
	}

}