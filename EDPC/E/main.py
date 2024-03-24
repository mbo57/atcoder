#!/usr/bin/env python3
N, W = map(int, input().split())

w = [0 for i in range(N)]
v = [0 for i in range(N)]

for i in range(N):
    w[i], v[i] = map(int, input().split())

dp = [[0 for i in range(W+1)] for i in range(N+1)]

limit = 1
for i in range(1, N+1):
    a = limit - 1
    if limit + w[i-1] > W + 1:
        b = W + 1
    else:
        limit += w[i-1]
        b = limit
    for j in range(a, b):
    # for j in range(W+1):
        print(i, j)
        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        if j - w[i-1] >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-w[i-1]] + v[i-1])
for i in dp:
    print(i)
print(dp[N][W])
