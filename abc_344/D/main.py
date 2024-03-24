#!/usr/bin/env python3
T = input()
N = int(input())
A = []
S = []
for i in range(N):
    tmp = list(input().split())
    A.append(int(tmp[0]))
    S.append(tmp[1:])
inf = 19999999999999
dp = [[inf for i in range(len(T)+1)] for i in range(N+1)]
for i in range(N+1):
    dp[i][0] = 0
# for i in range(len(T)+1):
#     dp[0][i] = 0

for i in range(1, N+1):
    for j in range(1, len(T)+1):
        for k in range(A[i-1]):
            num = len(S[i-1][k])
            if j - num < 0:
                continue
            # print(i, j, k, num)
            # print(T[j-num:j], S[i-1][k])
            # print(j-num, ":", j)
            if T[j-num:j] == S[i-1][k]:
                dp[i][j] = min(dp[i-1][j-num] + 1, dp[i-1][j], dp[i][j])
                # print(".main.py.swpaaaaaa", dp[i-1][j-num])
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j])
#                 print("bbbbbbbbb", dp[i-1][j-num])
#             print(i, j, dp[i][j])
#             print("__________________")
# for i in dp:
    # print(i)

if dp[N][len(T)] >= inf:
    print(-1)
else:
    print(dp[N][len(T)])
