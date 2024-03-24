#!/usr/bin/env python3


def solve(N, A):
    ans = []
    for i in range(N-1):
        ans.append(A[i] * A[i+1])
    return ans


def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, A)
    print(*[a[i] for i in range(N-1)])


if __name__ == '__main__':
    main()
