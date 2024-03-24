#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10 ** 6)

H, W = map(int, input().split())

li = [[] for i in range(H)]

for i in range(H):
    li[i] = list(input())

seen = [[0 for i in range(W)] for i in range(H)]
check = [-1, 0, 1]


def dfs(x, y):
    seen[x][y] = 1
    for i in check:
        for j in check:
            a = x - i
            b = y - j
            if (0 <= a < H and 0 <= b < W) and seen[a][b] != 1 and li[a][b] == "#":
                dfs(a, b)


ans = 0
for i in range(H):
    for j in range(W):
        if li[i][j] == ".":
            seen[i][j] = 1
        if seen[i][j] != 1:
            ans += 1
            dfs(i, j)

print(ans)
