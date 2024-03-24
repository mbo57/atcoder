package main

import (
	"fmt"
	"sort"
)

func main() {
	var n int
	var s []string
	var sc [][]int
	fmt.Scanf("%d", &n)
	for i := 0; i < n; i++ {
		var tmp string
		fmt.Scanf("%s", &tmp)
		cnt := 0
		for _, c := range tmp {
			if string([]rune{c}) == "x" {
				cnt += 1
			}
		}
		s = append(s, tmp)
		sc = append(sc, []int{cnt, i})
	}
	// fmt.Println(s)
	// fmt.Println(sc)
	sort.Slice(sc, func(i, j int) bool {
		p := sc[i]
		q := sc[j]
		if p[0] == q[0] {
			return sc[i][1] < sc[j][1]
		}
		return sc[i][0] < sc[j][0]
	})
	// fmt.Println(sc)
	for _, tmp := range sc {
		fmt.Printf("%d ", tmp[1]+1)
	}
}
