#!/usr/bin/env python3
import collections
import itertools
H, W = map(int, input().split())
A = []
A1 = []
for i in range(H):
    tmp = list(map(int, input().split()))
    A.append(tmp)
    A1 += tmp
B = []
B1 = []
di = {}
goal = {}
for i in range(H):
    tmp = list(map(int, input().split()))
    B.append(tmp)
    B1 += tmp
    for j in range(W):
        if A[i][j] != tmp[j]:
            if tmp[j] in goal:
                goal[tmp[j]].append((i, j))
            else:
                goal[tmp[j]] = [(i, j)]
            if A[i][j] in di:
                di[A[i][j]].append((i, j))
            else:
                di[A[i][j]] = [(i, j)]

Acnt = collections.Counter(A1)
Bcnt = collections.Counter(B1)
if Acnt != Bcnt:
    print(-1)
    exit(0)
if A == B:
    print(0)
    exit(0)

to = [[None for i in range(W)] for i in range(H)]
for tmp in di.keys():
    if len(di[tmp]) > 1:
        mcnt = 100000000000000
        for a in itertools.permutations(list(range(len(tmp))), len(tmp)):
            cnt = 0
            for ind, val in enumerate(a):
                cnt += abs(di[tmp][ind][0] - goal[tmp][val][0]) + abs(di[tmp][ind][1] - goal[tmp][val][1])
            mcnt = min(mcnt, cnt)
            if mcnt > cnt:
                mcnt = cnt
                saveto = a
        for ind, val in enumerate(saveto):
            to[di[tmp][ind][0]][di[tmp][ind][1]] = (goal[tmp][val][0], goal[tmp][val][1])
    else:
        to[di[tmp][0][0]][di[tmp][0][1]] = (goal[tmp][0][0], goal[tmp][0][1])
for i in to:
    print(i)

cnt = 0
for i in range(H):
    for j in range(W):
        if to[i][j] is None:
            continue

        a = to[i][j][0] - i
        b = to[i][j][1] - j
        if a > 0:
            if to[i+1][j] is None:
                continue
            aa = to[i+1][j][0] - (i + 1)
            if aa < 0:
                to[i][j], to[i+1][j] = to[i+1][j], to[i][j]
                cnt += 1
        if a < 0:
            if to[i-1][j] is None:
                continue
            aa = to[i-1][j][0] - (i - 1)
            if aa > 0:
                to[i][j], to[i-1][j] = to[i-1][j], to[i][j]
                cnt += 1

        if b > 0:
            if to[i][j+1] is None:
                continue
            bb = to[i][j+1][0] - (j + 1)
            if bb < 0:
                to[i][j], to[i][j+1] = to[i][j+1], to[i][j]
                cnt += 1
        if b < 0:
            if to[i][j-1] is None:
                continue
            bb = to[i][j-1][0] - (j - 1)
            if bb > 0:
                to[i][j], to[i][j-1] = to[i][j-1], to[i][j]
                cnt += 1
print("============", cnt)
for i in to:
    print(i)





