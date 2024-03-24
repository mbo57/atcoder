#!/usr/bin/env python3


def solve(N):
    tmp = N
    while True:
        a = tmp % 2 == 0
        b = tmp % 3 == 0
        if a:
            tmp = tmp // 2
        if b:
            tmp = tmp // 3
        if not a and not b:
            break
    if tmp == 1:
        return "Yes"
    else :
       return "No"


def main():
    N = int(input())
    a = solve(N)
    print(a)


if __name__ == '__main__':
    main()
