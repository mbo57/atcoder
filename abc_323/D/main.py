#!/usr/bin/env python3
N = int(input())
S = [0 for _ in range(N)]
C = [0 for _ in range(N)]
di = {}
for i in range(N):
    S[i], C[i] = map(int, input().split())
    di[S[i]] = C[i]

soS = sorted(S)
for i in range(N):
    size = soS[i]
    cnt = di[size]
    flag = True
    while cnt > 1:
        mod = cnt % 2
        cnt = cnt // 2
        di[size] = mod
        size = 2 * size
        if size in di:
            di[size] += cnt
            flag = False
            # print("#", di)
            break
        # print(di)
    if flag:
        di[size] = cnt
# for tmp in list(di.items()):
#     print(tmp)
print(sum(list(di.values())))
