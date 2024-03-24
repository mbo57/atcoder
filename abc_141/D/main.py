#!/usr/bin/env python3
import heapq


def solve(N, M, A):
    if N == 1:
        return A[0] // 2 ** M
    q = list(map(lambda x: x*(-1), A))
    heapq.heapify(q)
    for i in range(M):
        tmp = heapq.heappop(q)
        heapq.heappush(q, tmp / 2)
    # print(q)
    ans = [0 for i in range(N)]
    for i in range(N):
        ans[i] = int(heapq.heappop(q) * -1)
    # print(ans)
    return sum(ans)

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
