#!/usr/bin/env python3
N = int(input())
row = [None for i in range(N)]
col = [None for i in range(N)]
S = [None for i in range(N)]
for i in range(N):
    tmp = input()
    row[i] = tmp.count("o")
    S[i] = list(tmp)
ST = list(zip(*S))
for i in range(N):
    col[i] = ST[i].count("o")
# print(row)
# print(col)
ans = 0
for i in range(N):
    for j in range(N):
        if S[i][j] == "o" and row[i] > 0 and col[j] > 0:
            ans += (row[i] - 1) * (col[j] - 1)
print(ans)

