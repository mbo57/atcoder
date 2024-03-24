#!/usr/bin/env python3


def solve(N, S, K, P, Q):
    ans = 0
    for i in range(N):
        ans += P[i] * Q[i]
    if ans < S:
        ans += K
    return ans


def main():
    N, S, K = map(int, input().split())
    P = [None for _ in range(N)]
    Q = [None for _ in range(N)]
    for i in range(N):
        P[i], Q[i] = map(int, input().split())
    a = solve(N, S, K, P, Q)
    print(a)


if __name__ == '__main__':
    main()
