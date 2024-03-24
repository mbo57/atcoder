#!/usr/bin/env python3
from collections import deque
inf = 10 ** 10
N = int(input())
li = []
p = []
for i in range(N):
    tmp = list(input())
    for j in range(N):
        if tmp[j] == "P":
            p.append([i, j])
    li.append(tmp)

vec = [(1, 0), (0, 1), (-1, 0), (0, -1)]
p1x, p1y = p[0]
p2x, p2y = p[1]

G = [[[[inf for i in range(N)] for i in range(N)] for i in range(N)] for i in range(N)]
G[p1x][p1y][p2x][p2y] = 0
a = deque()
a.append((p1x, p1y, p2x, p2y))
ans = inf

while len(a) > 0:
    p1x, p1y, p2x, p2y = a.popleft()
    if p1x == p2x and p1y == p2y:
        ans = min(G[p1x][p1y][p1x][p1y], ans)
        break
    for i in range(4):
        x, y = vec[i]
        np1x = x + p1x
        np1y = y + p1y

        np2x = x + p2x
        np2y = y + p2y

        if np1x < 0:
            np1x = 0
        if np1x >= N:
            np1x = N - 1

        if np1y < 0:
            np1y = 0
        if np1y >= N:
            np1y = N - 1

        if np2x < 0:
            np2x = 0
        if np2x >= N:
            np2x = N - 1

        if np2y < 0:
            np2y = 0
        if np2y >= N:
            np2y = N - 1

        if li[np1x][np1y] == "#":
            np1x = p1x
            np1y = p1y
        if li[np2x][np2y] == "#":
            np2x = p2x
            np2y = p2y

        if G[p1x][p1y][p2x][p2y] + 1 < G[np1x][np1y][np2x][np2y]:
            G[np1x][np1y][np2x][np2y] = G[p1x][p1y][p2x][p2y] + 1
            a.append((np1x, np1y, np2x, np2y))
        # print(G)
if ans == inf:
    print(-1)
    exit(0)
print(ans)
