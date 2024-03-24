#!/usr/bin/env python3


def solve(N):
    ans = ""
    for i in range(N):
        ans += "10"
    return ans + "1"


def main():
    N = int(input())
    a = solve(N)
    print(a)


if __name__ == '__main__':
    main()
