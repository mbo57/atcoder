#!/usr/bin/env python3
N, X = map(int, input().split())
T = list(map(int, input().split()))

mod = 998244353
inv = pow(N, mod - 2, mod)

dp = [0 for i in range(X+1)]
dp[0] = 1

ans = 0
if T[0] > X:
    ans += 1

for i in range(1, X+1):
    for j in range(N):
        if i - T[j] >= 0:
            dp[i] = (dp[i] + (dp[i - T[j]] * inv) % mod) % mod
    if X - T[0] < i:
        ans = (ans + dp[i]) % mod

print((ans * inv) % mod)
