package main

import (
    . "fmt"
  //  "runtime"
    "time"
)

	var i int = 0
	var channel = make(chan int,1)
	var a,b int;

func someGoroutine1() {	
	for x := 0; x < 1000000; x++ {
		a = <-channel      
		a++
		channel <- a
    	} 
}

func someGoroutine2() {
	for y := 0; y < 1000001; y++ {
		b = <-channel        
		b--
		channel <- b
    	} 
}

func main() {
	//runtime.GOMAXPROCS(runtime.NumCPU())                             
	
	channel <- i

	go someGoroutine1()
	go someGoroutine2()

	time.Sleep(1000*time.Millisecond)

	i = <-channel
	Println(i)
}
