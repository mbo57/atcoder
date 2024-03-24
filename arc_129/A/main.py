#!/usr/bin/env python3


def solve(N, L, R):
    binary = bin(N)
    length = len(binary[2:])
    # print(binary, length)
    ans = 2 ** (length - 1) + (N - 2 ** (length - 1))
    return ans


def main():
    N, L, R = map(int, input().split())
    a = solve(N, L, R)
    print(a)


if __name__ == '__main__':
    main()
