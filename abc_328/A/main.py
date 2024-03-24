#!/usr/bin/env python3


def solve(N, X, S):
    ans = 0
    for i in range(N):
        if S[i] <= X:
            ans += S[i]
    return ans


def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    X = int(next(tokens))
    S = [None for _ in range(N)]
    for i in range(N):
        S[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, X, S)
    print(a)


if __name__ == '__main__':
    main()
