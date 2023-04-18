package main

import (
    "fmt"
    "time"
)

func odd(ch chan int, n int) {
    i := 1
    for i <= n {
        ch <- i
        fmt.Println(<-ch)
        i += 2
    }
}

func even(ch chan int, n int) {
    i := 2
    for i <= n {
        fmt.Println(<-ch)
        ch <- i
        i += 2
    }
}

func main() {
    ch := make(chan int)

    go odd(ch, 10)
    go even(ch, 10)

    // To wait for 2 threads, better option is to use sync.WaitGroup
    time.Sleep(2 * time.Second)
}
