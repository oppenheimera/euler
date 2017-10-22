package main 

import (
    "fmt"
    // "math"
)

func getlayer(s []int, n int) []int {
    return append(s, n)
}

func main() {
    s := []int{0,1,2,3}
    fmt.Println(getlayer(s, 4))
}