package main

import (
	"fmt"
	"os"
)

func main() {
	var s string
	fmt.Scanf("%s", &s)

	for i := 1; i < 16; i++ {
		if i%2 == 1 && string(s[i]) == "1" {
			fmt.Println("No")
			os.Exit(0)
		}
	}
	fmt.Println("Yes")
}
