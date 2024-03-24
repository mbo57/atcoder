#!/usr/bin/env python3
N, Q = map(int, input().split())
R = list(map(int, input().split()))
sR = sorted(R)
li = [0]
tmp = 0
for i in range(N):
    tmp += sR[i]
    li.append(tmp)
li.append(li[-1]+1)
# print(li)
for i in range(Q):
    x = int(input())
    l = 0
    r = N + 1
    while r - l > 1:
        m = (r + l) // 2
        if li[m] <= x:
            l = m
        else:
            r = m
        # print(l, m, r)
    print(l)

