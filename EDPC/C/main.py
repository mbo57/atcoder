#!/usr/bin/env python3
N = int(input())
s = [[] for i in range(N)]

for i in range(N):
    s[i] = list(map(int, input().split()))

dp = [[0, 0, 0] for i in range(N+1)]
for i in range(1, N+1):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i][j] = max(dp[i][j], dp[i-1][k] + s[i-1][k])
print(max(dp[N]))

