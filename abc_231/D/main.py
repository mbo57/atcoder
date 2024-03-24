#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)

seen = [0 for i in range(N)]

for i in range(N):
    if len(G[i]) > 2:
        print("No")
        exit(0)


def dfs(before, x):
    # print(before, x)
    seen[x] = 1
    for i in G[x]:
        if i == before:
            continue
        if seen[i] == 1:
            print("No")
            exit(0)
        dfs(x, i)


for i in range(N):
    if seen[i] == 0:
        dfs(None, i)
print("Yes")
