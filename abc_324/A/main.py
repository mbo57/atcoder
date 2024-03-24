#!/usr/bin/env python3


def solve(N, A):
    if len(set(A)) == 1:
        return "Yes"
    else:
        return "No"


def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, A)
    print(a)


if __name__ == '__main__':
    main()
