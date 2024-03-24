package main

import (
	"fmt"
	"sort"
)

func main() {
	var n int
	var s, c []int
	di := make(map[int]int)
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		var ts, tc int
		fmt.Scan(&ts, &tc)
		s = append(s, ts)
		c = append(c, tc)
		di[ts] = tc
	}
	sort.Slice(s, func(i, j int) bool { return s[i] < s[j] })
	ans := 0
	for _, num := range s {
		size := num
		cnt := di[size]
		for cnt > 0 {
			mod := cnt % 2
			cnt = cnt / 2
			ans += mod
			size *= 2
			if _, ok := di[size]; ok {
				di[size] += cnt
				break
			}
			if cnt == 1 {
				ans += 1
				break
			}
		}
	}
	fmt.Println(ans)
}
