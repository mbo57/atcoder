#!/usr/bin/env python3
N, Q = map(int, input().split())
S = input()

li = [0 for i in range(N)]
cnt = 0
for i in range(1, N):
    if S[i] == S[i-1]:
        cnt += 1
    li[i] = cnt

# print(li)
for i in range(Q):
    l, r = map(int, input().split())
    print(li[r-1] - li[l-1])
