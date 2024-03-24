#!/usr/bin/env python3
import heapq
N = int(input())

di = {}
t = {}

for i in range(N):
    T, D = map(int, input().split())
    t[i] = D
    if T in di:
        di[T][0].append(i)
    else:
        di[T] = [[i], []]
    if T+D in di:
        di[T+D][1].append(i)
    else:
        di[T+D] = [[], [i]]

k = sorted(list(di.keys()))
# print(di)
# print(k)
li = []
end = set()

ans = 0

for i in range(len(k)):
    # print("#", k[i])
    tmp = k[i] - k[i-1] - 1
    # print(tmp)
    while len(li) > 0 and tmp > 0:
        a = heapq.heappop(li)
        if a[1] not in end:
            end.add(a[1])
            ans += 1
            tmp -= 1
    for j in di[k[i]][0]:
        heapq.heappush(li, [k[i] + t[j], j])
    while len(li) > 0:
        a = heapq.heappop(li)
        if a[1] not in end:
            # print(a)
            ans += 1
            break
    for j in di[k[i]][1]:
        end.add(j)
    # print(end)
    # print("ans", ans)
print(ans)    
