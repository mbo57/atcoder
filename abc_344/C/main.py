#!/usr/bin/env python3


def solve(N, A, M, B, L, C, Q, X):
    ans = ["No" for i in range(Q)]
    se = set()
    for n in range(N):
        for m in range(M):
            for l in range(L):
                se.add(A[n] + B[m] + C[l])
    for q in range(Q):
        if X[q] in se:
            ans[q] = "Yes"
    return ans


def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    M = int(next(tokens))
    B = [None for _ in range(M)]
    for i in range(M):
        B[i] = int(next(tokens))
    L = int(next(tokens))
    C = [None for _ in range(L)]
    for i in range(L):
        C[i] = int(next(tokens))
    Q = int(next(tokens))
    X = [None for _ in range(Q)]
    for i in range(Q):
        X[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, A, M, B, L, C, Q, X)
    for i in range(Q):
        print(a[i])


if __name__ == '__main__':
    main()
