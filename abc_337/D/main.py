#!/usr/bin/env python3
H, W, K = map(int, input().split())
li = []
for i in range(H):
    tmp = list(input())
    li.append(tmp)

ans = 10000000000000000000000

for i in range(H):
    cnt = 0
    cntdot = 0
    for j in range(W):
        if cntdot + cnt >= K:
            if li[i][j - K] == "o":
                cnt -= 1
            elif li[i][j - K] == ".":
                cntdot -= 1
        if li[i][j] == "o":
            cnt += 1
        elif li[i][j] == "x":
            cnt = 0
            cntdot = 0
        elif li[i][j] == ".":
            cntdot += 1
        # print(i, j, cnt, cntdot)
        if cntdot + cnt >= K:
            # print("aaaaaaaaaa")
            ans = min(ans, cntdot)
li = list(zip(*li))
for i in range(W):
    cnt = 0
    cntdot = 0
    for j in range(H):
        if cntdot + cnt >= K:
            if li[i][j - K] == "o":
                cnt -= 1
            elif li[i][j - K] == ".":
                cntdot -= 1
        if li[i][j] == "o":
            cnt += 1
        elif li[i][j] == "x":
            cnt = 0
            cntdot = 0
        elif li[i][j] == ".":
            cntdot += 1
        if cntdot + cnt == K:
            ans = min(ans, cntdot)
if ans == 10000000000000000000000:
    print(-1)
else:
    print(ans)
