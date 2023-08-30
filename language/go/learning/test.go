package main

import (
	"fmt"
	"os"
)

func main() {
	defer fmt.Println("Deferred function")
	fmt.Println("Starting program")
	os.Exit(3)
	fmt.Println("This line will not be executed")
}
