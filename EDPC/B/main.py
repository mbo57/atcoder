#!/usr/bin/env python3
N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [10**20 for i in range(N)]
dp[0] = 0
for i in range(N):
    for j in range(min(i, K)):
        dp[i] = min(dp[i], dp[i-j-1] + abs(h[i] - h[i-j-1]))
print(dp[N-1])
