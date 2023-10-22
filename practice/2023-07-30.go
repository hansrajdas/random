package main

import "fmt"

func main() {
    f1()
}

func f1() {
    ch := make(chan int)
    go func () {
        for i := 1; i <= 5; i++ {
            ch <- i
        }
        close(ch)
    }()

    for i := 0; i < 10; i++ {
        x, y := <-ch
        fmt.Println(x, y)
    }
}
