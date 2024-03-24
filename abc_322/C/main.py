#!/usr/bin/env python3


def solve(N, M, A):
    setA = set(A)
    ans = [0 for i in range(N)]
    cnt = 0
    for i in reversed(range(N)):
        if i + 1 in setA:
            cnt = 0
        else:
            cnt += 1
        ans[i] = cnt
    return ans



def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    M = int(next(tokens))
    A = [None for _ in range(M)]
    for i in range(M):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    ans = solve(N, M, A)
    for i in range(N):
        print(ans[i])


if __name__ == '__main__':
    main()
