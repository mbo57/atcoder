#!/usr/bin/env python3


def solve(N, M, S):
    maxb = 0
    a = 0
    b = 0
    for i in range(N):
        if S[i] == "0":
            a = 0
            maxb = max(maxb, b)
            b = 0
        elif S[i] == "1":
            if a < M:
                a += 1
            else:
                b += 1
        else:
            b += 1
    maxb = max(maxb, b)
    return maxb


def main():
    N, M = map(int, input().split())
    S = input()
    b = solve(N, M, S)
    print(b)


if __name__ == '__main__':
    main()
