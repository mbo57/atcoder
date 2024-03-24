#!/usr/bin/env python3


def solve(N, L, A):
    ans = 0
    for i in range(N):
        if A[i] >= L:
            ans += 1
    return ans


def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    L = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, L, A)
    print(a)


if __name__ == '__main__':
    main()
