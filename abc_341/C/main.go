package main

import (
	"fmt"
	"strings"
)

func main() {
	var tmp string
	var h, w, n int
	var s [][]string
	fmt.Scanf("%d %d %d", &h, &w, &n)
	fmt.Scanf("%s", &tmp)
	t := strings.Split(tmp, "")
	// fmt.Println(h, w, n)
	// fmt.Println(t)
	for i := 0; i < h; i++ {
		fmt.Scanf("%s", &tmp)
		s = append(s, strings.Split(tmp, ""))
	}
	// fmt.Printf("%+v\n", s)

	ans := 0
	for i := 0; i < h; i++ {
		for j := 0; j < w; j++ {
			if s[i][j] == "#" {
				continue
			}
			x := i
			y := j
			ok := true
			for _, c := range t {
				switch c {
				case "U":
					x--
				case "D":
					x++
				case "L":
					y--
				case "R":
					y++
				}
				if s[x][y] == "#" {
					ok = false
					break
				}
			}
			if ok {
				ans++
			}
		}
	}
	fmt.Println(ans)
}
