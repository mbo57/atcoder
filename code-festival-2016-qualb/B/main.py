#!/usr/bin/env python3
N, A, B = map(int, input().split())
S = input()

cntA = 0
cntB = 0
for i in range(N):
    if S[i] == "a":
        if cntA + cntB < A + B:
            cntA += 1
            print("Yes")
        else:
            print("No")
    elif S[i] == "b":
        if cntA + cntB < A + B and cntB < B:
            cntB += 1
            print("Yes")
        else:
            print("No")
    else:
        print("No")
