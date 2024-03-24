#!/usr/bin/env python3
import heapq
N, M, K = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    u, v, w = map(int, input().split())
    G[u-1].append((v-1, w))
    G[v-1].append((u-1, w))

used = [False] * N
cnt = 0
ans = 0
q = [(0, 0)]
while cnt < N:
    # print(q)
    d, v = heapq.heappop(q)
    if used[v]:
        continue
    used[v] = True
    cnt += 1
    # ans = (ans + d) % K
    ans += d
    print(v+1, d)
    for nv, c in G[v]:
        if used[nv]:
            continue
        heapq.heappush(q, (c, nv))

print(ans)
print(K)
print(ans % K)
