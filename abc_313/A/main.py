#!/usr/bin/env python3


def solve(N, P):
    if N == 1:
        return 0
    p1 = P[0]
    Psort = sorted(P[1:])
    pmax = Psort[-1]
    if p1 > pmax:
        return 0
    else:
        return pmax - p1 + 1


def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    P = [None for _ in range(N)]
    for i in range(N):
        P[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, P)
    print(a)


if __name__ == '__main__':
    main()
