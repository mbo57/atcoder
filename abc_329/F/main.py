#!/usr/bin/env python3
N, Q = map(int, input().split())
C = list(map(int, input().split()))

li = [{C[i]} for i in range(N)]

for i in range(Q):
    a, b = map(int, input().split())
    A = li[a-1]
    B = li[b-1]
    if len(li[a-1]) > len(li[b-1]):
        li[a-1] |= li[b-1]
        li[b-1] = set()
        li[a-1], li[b-1] = li[b-1], li[a-1]
    else:
        li[b-1] |= li[a-1]
        li[a-1] = set()
    li[b-1] = A | B
    li[a-1] = set()
    print(len(li[b-1]))
