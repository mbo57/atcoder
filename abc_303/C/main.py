#!/usr/bin/env python3

N, M, H, K = map(int, input().split())
S = input()
heal = set()
for i in range(M):
    x, y = map(int, input().split())
    heal.add((x, y))

mv = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}
X = 0
Y = 0
for i in range(N):
    X += mv[S[i]][0]
    Y += mv[S[i]][1]
    H -= 1
    if H < 0:
        print("No")
        exit()
    if (X, Y) in heal and H < K:
        H = K
        heal.remove((X, Y))
print("Yes")
