#!/usr/bin/env python3


def solve(N):
    return "L" + "o" * N + "n" + "g"


def main():
    N = int(input())
    a = solve(N)
    print(a)


if __name__ == '__main__':
    main()
