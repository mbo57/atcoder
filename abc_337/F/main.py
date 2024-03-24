#!/usr/bin/env python3


def solve(N, M, K, C):


def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    M = int(next(tokens))
    K = int(next(tokens))
    C = [None for _ in range(N)]
    for i in range(N):
        C[i] = int(next(tokens))
    assert next(tokens, None) is None
    X = solve(N, M, K, C)
    for i in range(N):
        print(X[i])


if __name__ == '__main__':
    main()
