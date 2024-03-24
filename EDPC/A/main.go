package main

import (
	"fmt"
	"math"
)

func main() {
	var n int
	fmt.Scan(&n)
	h := make([]int, n)
	for i := 0; i < n; i++ {
		var tmp int
		fmt.Scan(&tmp)
		h[i] = tmp
	}

	dp := make([]int, n)
	dp[0] = 0
	dp[1] = int(math.Abs(float64(h[0]) - float64(h[1])))
	for i := 2; i < n; i++ {
		a := dp[i-1] + int(math.Abs(float64(h[i])-float64(h[i-1])))
		b := dp[i-2] + int(math.Abs(float64(h[i])-float64(h[i-2])))
		if a > b {
			a = b
		}
		dp[i] = a
	}
	fmt.Println(dp[n-1])
}
