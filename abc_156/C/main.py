#!/usr/bin/env python3


def solve(N, X):
    maxX = max(X)
    ans = 10000000000000
    for i in range(1, maxX+1):
        s = 0
        for j in range(N):
            s += (X[j] - i) ** 2
        if ans > s:
            ans = s
    return ans


def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    X = [None for _ in range(N)]
    for i in range(N):
        X[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, X)
    print(a)


if __name__ == '__main__':
    main()
