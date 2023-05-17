package main

import (
    "fmt"
    "sync"
)

func main() {
    times := 5
    var wg sync.WaitGroup
    ch := make(chan string)
    wg.Add(2)

    go func(n int) {
        defer wg.Done()
        for i := 0; i < n; i++ {
            fmt.Println(<-ch)
            ch <- "pong"
        }
    }(times)

    go func(n int) {
        defer wg.Done()
        for i := 0; i < n; i++ {
            ch <- "ping"
            fmt.Println(<-ch)
        }
    }(times)

    wg.Wait()
}
