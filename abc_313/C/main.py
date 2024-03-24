#!/usr/bin/env python3


def solve(N, A):
    A = sorted(A)
    Asum = sum(A)
    q = Asum // N
    r = Asum % N
    B = [q for i in range(N-r)] + [q + 1 for i in range(r)]
    S = 0
    for i in range(N):
        S += abs(A[i] - B[i])
    return S // 2


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
