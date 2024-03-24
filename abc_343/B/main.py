#!/usr/bin/env python3
N = int(input())
A = []
for i in range(N):
    tmp = list(map(int, input().split()))
    A.append(tmp)

for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            print(j + 1, end=" ")
    print()
