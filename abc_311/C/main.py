#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
N = int(input())
A = list(map(int, input().split()))
G = [[] for i in range(N)]
for i in range(N):
    G[i].append(A[i] - 1)

seen = [0 for i in range(N)]


def dfs(x, ans):
    seen[x] = 1
    for i in G[x]:
        if seen[i] == 1:
            ans.append(i)
            return ans
        ans.append(i)
        ans = dfs(i, ans)
    return ans


for i in range(N):
    tmp = dfs(i, [i])
    # print(tmp)
    di = {i: [False]for i in range(N)}
    for j in range(len(tmp)):
        # print(di)
        if di[tmp[j]][0]:
            print(j - di[tmp[j]][1])
            print(" ".join([str(x + 1) for x in tmp[di[tmp[j]][1]:j]]))
            exit()
        di[tmp[j]][0] = True
        di[tmp[j]].append(j)
    # print(tmp)
    # if tmp[0] == tmp[-1]:
    #     print(len(tmp[:-1]))
    #     print(" ".join([str(x + 1) for x in tmp[:-1]]))
    #     exit()
