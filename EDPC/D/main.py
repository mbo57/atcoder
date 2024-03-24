#!/usr/bin/env python3
N, W = map(int, input().split())

w = [0 for i in range(N)]
v = [0 for i in range(N)]

for i in range(N):
    w[i], v[i] = map(int, input().split())

dp = [[0 for i in range(N+1)] for i in range(W+1)]

for i in range(W+1):
    for j in range(1, N+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        if i - w[j-1] >= 0:
            dp[i][j] = max(dp[i][j], dp[i-w[j-1]][j-1] + v[j-1])
print(dp[W][N])
