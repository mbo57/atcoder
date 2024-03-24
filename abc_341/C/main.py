#!/usr/bin/env python3
H, W, N = map(int, input().split())
S = [None for _ in range(H)]
T = input()
for i in range(H):
    S[i] = input()

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            continue
        x = i
        y = j
        ok = True
        for k in list(T):
            if k == "U":
                x -= 1
            elif k == "D":
                x += 1
            elif k == "L":
                y -= 1
            elif k == "R":
                y += 1
            if S[x][y] == "#":
                ok = False
                break
        if ok:
            # print(i, j, S[i][j])
            ans += 1
print(ans)
