#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)

H, W = map(int, input().split())
li = []
for i in range(H):
    li.append(list(input()))

seen = [[0 for i in range(W)] for i in range(H)]

ne = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def check(x, y, nx, ny):
    while True:
        x += nx
        y += ny
        if x > H - 1 or y > W - 1 or x < 0 or y < 0:
            x -= nx
            y -= ny
            break
        if li[x][y] == "#":
            x -= nx
            y -= ny
            break
        else:
            if seen[x][y] != 2:
                seen[x][y] = 1
    if seen[x][y] != 2:
        seen[x][y] = 2
        find(x, y)


def find(x, y):
    for nx, ny in ne:
        # print("=============")
        # print(x, y)
        # print(nx, ny)
        check(x, y, nx, ny)

find(1, 1)
# def dfs(x, y):
#     seen[x][y] = 1
import numpy as np
tmp = np.array(seen)
print(np.count_nonzero(tmp > 0))
# print(seen)

for i in li:
    print(i)
for i in seen:
    print([str(j) for j in i])
