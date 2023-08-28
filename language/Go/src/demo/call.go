package main

import (
    "fmt"
)

type Phone interface {
    call()
}

type NokiaPhone struct {
}

func (nokiaPhone NokiaPhone) call() {
    fmt.Println("I am Nokia, I can call you!")
}

type IPhone struct {
}

func (iPhone IPhone) call() {
    fmt.Println("I am iPhone, I can call you!")
}


type max struct{

}
func (m max) call(){
	fmt.Printf("test\n")
}

func main() {

	// fmt.Println("c = ", c)
    var phone Phone

    phone = new(NokiaPhone)
    phone.call()
	phone = new(max)
	phone.call()

    // phone = new(IPhone)
    // phone.call()

}