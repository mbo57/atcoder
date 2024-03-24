#!/usr/bin/env python3


def solve(N, W, X):
    ans = [0 for i in range(24)]
    for i in range(N):
        tmp = (9 - X[i]) % 24
        for j in range(9):
            time = (tmp + j) % 24
            ans[time] += W[i]
    return max(ans)


def main():
    N = int(input())
    W = [None for _ in range(N)]
    X = [None for _ in range(N)]
    for i in range(N):
        W[i], X[i] = map(int, input().split())
    a = solve(N, W, X)
    print(a)


if __name__ == '__main__':
    main()
