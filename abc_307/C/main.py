#!/usr/bin/env python3
WA, HA = map(int, input().split())
A = []
for i in range(HA):
    A.append(list(map(int, input().split())))

WB, HB = map(int, input().split())
B = []
for i in range(HB):
    B.append(list(map(int, input().split())))

WX, HC = map(int, input().split())
X = []
for i in range(HA):
    X.append(list(map(int, input().split())))

C = [["." for i in range(WX)] for i in range(HX)]
for i in range(HX):
    for j in range(WX):
        if X[i][j] == "#":
            A


