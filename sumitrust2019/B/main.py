#!/usr/bin/env python3


def solve(N):
    a = int(N // 1.08)
    b = int((N + 1.08) // 1.08)
    # print(a, b)
    # print(a * 1.08, b * 1.08)
    if int(a * 1.08) == N:
        return int(a)
    if int(b * 1.08) == N:
        return int(b)
    return ":("


def main():
    N = int(input())
    a = solve(N)
    print(a)


if __name__ == '__main__':
    main()
