#!/usr/bin/env python3


def solve(N, K, A):
    sA = sorted(set(A))
    if sA[-1] <= K:
        return (K + 1) * K // 2 - sum(sA)
    for i in range(len(sA)):
        if sA[i] > K:
            break
    # print(sA[:i])
    return (K + 1) * K // 2 - sum(sA[:i])


def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    K = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, K, A)
    print(a)


if __name__ == '__main__':
    main()
