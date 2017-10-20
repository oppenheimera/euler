package main 

import (
    "math"
    "fmt"
)

m := map[int]int{1:1}

func streak(n int) int {
    i := 1
    if val, ok := m[n]; ok {
        return m[val]
    }
    for n % i == 0 {
        n += 1
        i += 1
    }
    return i - 1
}

func P(s, N int) (count int) {
    for n := 1; n < N; n++ {
        if streak(n) == s {
            count += 1
        }
    }
    return
}

func main() {
    // sum := 0
    math.Pow(float64(4), float64(2))
    // for i := 1; i <= 31; i++ {
    //     limit := int(math.Pow(float64(4), float64(i)))
    //     sum += P(i, limit)
    // }
    fmt.Println(streak(13))
}