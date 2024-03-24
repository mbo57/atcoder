#!/usr/bin/env python3
import heapq
Q = int(input())

li = []
add = 0
for i in range(Q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        heapq.heappush(li, que[1] - add)
    elif que[0] == 2:
        add += que[1]
    elif que[0] == 3:
        tmp = heapq.heappop(li)
        print(tmp + add)
