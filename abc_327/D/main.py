#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10 ** 9)
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

G = [set() for i in range(N)]
for i in range(M):
    G[A[i]-1].add(B[i]-1)
    G[B[i]-1].add(A[i]-1)


def dfs(x, tmp):
    seen[x] = tmp
    for nx in G[x]:
        if seen[nx] == tmp:
            print("No")
            exit(0)
        if seen[nx] != -1:
            continue
        dfs(nx, (tmp + 1) % 2)


seen = [-1 for i in range(N)]
for i in range(N):
    if seen[i] == -1:
        dfs(i, 0)
print("Yes")
