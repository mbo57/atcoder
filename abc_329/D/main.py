#!/usr/bin/env python3
import heapq


def solve(N, M, A):
    li = []
    di = {0: 0}
    ans = []
    f = 0
    for i in range(M):
        a = A[i]
        if a in di:
            di[a] += 1
        else:
            di[a] = 1
        if di[f] < di[a]:
            f = a
        elif di[f] == di[a]:
            f = min(f, a)
        ans.append(f)
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
    for i in range(M):
        print(ans[i])


if __name__ == '__main__':
    main()
