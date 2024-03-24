#!/usr/bin/env python3


def solve(N, P, Q, D):
    return min(Q + min(D), P)


def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    P = int(next(tokens))
    Q = int(next(tokens))
    D = [None for _ in range(N)]
    for i in range(N):
        D[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, P, Q, D)
    print(a)


if __name__ == '__main__':
    main()
