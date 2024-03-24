#!/usr/bin/env python3
from collections import deque
N, M = map(int, input().split())

G = [[] for i in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    G[A - 1].append(B - 1)
    G[B - 1].append(A - 1)

ans = [-2 for i in range(N)]
ans[0] = -1

q = deque([0])


while len(q) > 0:
    x = q.popleft()
    for nx in G[x]:
        if ans[nx] != -2:
            continue
        ans[nx] = x
        q.append(nx)

print("Yes")
for i in range(1, N):
    print(ans[i] + 1)
