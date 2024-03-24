package main

import (
	"fmt"
	"sort"
)

func main() {
	var n int
	var m int
	var a []int
	var aWIndex [][]int
	fmt.Scanf("%d %d", &n, &m)
	for i := 0; i < m; i++ {
		var tmp int
		fmt.Scan(&tmp)
		a = append(a, tmp)
		aWIndex = append(aWIndex, []int{tmp, i})
	}
	// fmt.Println(a)
	var s []string
	var sc []int
	for i := 0; i < n; i++ {
		var tmp string
		fmt.Scan(&tmp)
		s = append(s, tmp)
		sc = append(sc, i+1)
		for j := 0; j < m; j++ {
			if string(tmp[j]) == "o" {
				sc[i] += a[j]
			}
		}
	}
	// fmt.Println(a)
	// fmt.Println(s)
	var scmax int
	for i := 0; i < n; i++ {
		if scmax < sc[i] {
			scmax = sc[i]
		}
	}
	sort.Slice(aWIndex, func(i, j int) bool {
		return aWIndex[i][0] > aWIndex[j][0]
	})
	// fmt.Println(aWIndex)
	var ans []int
	for i := 0; i < n; i++ {
		ans = append(ans, 0)
		for j := 0; j < m; j++ {
			if sc[i] < scmax {
				if string(s[i][aWIndex[j][1]]) == "x" {
					sc[i] += aWIndex[j][0]
					ans[i] += 1
				}
			} else {
				break
			}
		}
	}
	for i := 0; i < n; i++ {
		fmt.Printf("%d\n", ans[i])
	}

}

// def solve(N, M, A, S):
//     sc = [i + 1 for i in range(N)]
//     for i in range(N):
//         for j in range(M):
//             if S[i][j] == "o":
//                 sc[i] += A[j]
//     maxsc = max(sc)
//     li = []
//     for i in range(M):
//         li.append([A[i], i])
//     soA = sorted(li, reverse=True)
//     ans = [0 for i in range(N)]
//     for i in range(N):
//         for j in range(M):
//             if sc[i] < maxsc:
//                 if S[i][soA[j][1]] == "x":
//                     sc[i] += soA[j][0]
//                     ans[i] += 1
//             else:
//                 break
//             # print(i, sc[i])
//     return ans
