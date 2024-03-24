#!/usr/bin/env python3
from collections import deque

N, M = map(int, input().split())

pair = []
for i in range(int(M**(1/2))+1):
    for j in range(i, int(M**(1/2))+1):
        tmp = i ** 2 + j ** 2
        if tmp == M:
            pair.append((i, j))
# print(pair)

li = [[-1 for i in range(N)] for i in range(N)]
li[0][0] = 0


q = deque([])
q.append((0, 0, 0))
while len(q) > 0:
    x, y, s = q.popleft()
    for i in range(len(pair)):
        num = 8
        if pair[i][0] == 0:
            num = 4
        a = pair[i][0]
        b = pair[i][1]
        vec = ((a, b), (b, a), (a, -b), (-b, a), (-a, b), (b, -a), (-a, -b), (-b, -a))
        for i in range(num):
            addx, addy = vec[i]
            nx = x + addx
            ny = y + addy
            if nx < 0 or N - 1 < nx or ny < 0 or N - 1 < ny:
                continue
            if li[nx][ny] != -1:
                continue
            li[nx][ny] = s + 1
            # for i in range(N):
            #     # print(" ".join(list(map(str, li[i]))))
            # print("==========")
            q.append((nx, ny, s + 1))

for i in range(N):
    print(" ".join(list(map(str, li[i]))))
