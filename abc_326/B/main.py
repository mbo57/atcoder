#!/usr/bin/env python3


def solve(N):
    for i in range(N, 920):
        t = str(i)
        if int(t[0]) * int(t[1]) == int(t[2]):
            return i



def main():
    N = int(input())
    a = solve(N)
    print(a)


if __name__ == '__main__':
    main()
