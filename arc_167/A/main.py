#!/usr/bin/env python3


def solve(N, M, A):
    Aso = sorted(A, reverse=True)
    tmp1 = list(reversed(Aso[:M]))
    tmp2 = Aso[M:]
    for i in range(len(tmp2)):
        tmp1[i] += tmp2[i]
    ans = 0
    for i in range(M):
        ans += tmp1[i] * tmp1[i]
    return ans




def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    M = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, M, A)
    print(a)


if __name__ == '__main__':
    main()
