#!/usr/bin/env python3
N, D = map(int, input().split())
li = []
for i in range(N):
    tmp = list(input())
    li.append(tmp)

li = list(zip(*li))
# print(li)

ans = 0
cnt = 0
# tmp = tuple(["o" for i in range(N)])
# print(tmp)
for i in range(D):
    flag = True
    for j in li[i]:
        # print(j)
        if j == "x":
            flag = False
            break
    if flag:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
print(max(cnt, ans))
