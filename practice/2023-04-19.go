package main

import (
    "fmt"
    "sync"
)


type Vertex struct {
    x float64
    y float64
}

func init() {
    fmt.Println("In init")
}

func vFunc(v Vertex) float64 {
    return v.x + v.y
}

func (v Vertex) zFunc() float64 {
    return v.x + v.y
}

type I interface{
    M()
}

type T struct {
    S string
}

func (t T) M() {
    fmt.Println(t.S)
}

func do(i interface{}) {
    switch v := i.(type) {
    case int:
        fmt.Printf("%d is int\n", v)
    case string:
        fmt.Printf("%s is string\n", v)
    default:
        fmt.Printf("%v type is unknown\n", v)
    }
}

func sum(s []int, c chan int) {
    var sum int
    for _, v := range s {
        sum += v
    }
    c <- sum
}

func main() {
    v := Vertex{4, 5}
    s := &Vertex{4, 5}
    fmt.Println(vFunc(v))
    fmt.Println(v.zFunc())
    fmt.Println(s.zFunc())

    t := T{"Hello"}
    t.M()

    do(1)
    do("this is string")
    do(1.2)

    nums := []int{7, 2, 8, -9, 4, 0}
    c := make(chan int)
    go sum(nums[:len(nums)/2], c)
    go sum(nums[len(nums)/2:], c)
    x, y := <-c, <-c
    fmt.Println(x, y, x + y)

    // Ping pong example
    n := 5
    var wg sync.WaitGroup
    wg.Add(2)
    ch := make(chan string)
    go func(n int) {
        defer wg.Done()
        for i := 0; i < n; i++ {
            fmt.Println(<-ch)
            ch <- "pong"
        }
    }(n)
    go func(n int) {
        defer wg.Done()
        for i := 0; i < n; i++ {
            ch <- "ping"
            fmt.Println(<-ch)
        }
    }(n)
    wg.Wait()
}
