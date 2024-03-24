#!/usr/bin/env python3


def solve(N, L, R, A):
    ans = [None for i in range(N)]
    for i in range(N):
        if L <= A[i] <= R:
            ans[i] = A[i]
        elif A[i] < L:
            ans[i] = L
        else:
            ans[i] = R
    return ans



def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    L = int(next(tokens))
    R = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    ans = solve(N, L, R, A)
    print(*[ans[i] for i in range(N)])


if __name__ == '__main__':
    main()
