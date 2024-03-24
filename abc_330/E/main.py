#!/usr/bin/env python3
N, Q = map(int, input().split())
A = list(map(int, input().split()))

sortA = sorted(set(A))
di = {}
flag = True
for i in range(N):
    if flag and sortA[i] != i:
        mex = i
        flag = False
    if A[i] in di:
        di[A[i]] += 1
    else:
        di[A[i]] = 1

print(di, mex)

for i in range(Q):
    ii, x = map(int, input().split())
    ii -= 1
    tmp = A[ii]
    A[ii] = x
    di[tmp] -= 1
    if A[ii] in di:
        di[A[ii]] += 1
    else:
        di[A[ii]] = 1
    if di[tmp] == 0 and mex > tmp:
        mex = tmp
    print(mex)
