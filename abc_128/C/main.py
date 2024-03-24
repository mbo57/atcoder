#!/usr/bin/env python3
N, M = map(int, input().split())
s = []
d = [[] for i in range(N)]
for i in range(M):
    s.append(list(map(int, input().split())))
    for j in s[i][1:]:
        d[j-1].append(i)
p = list(map(int, input().split()))

cnt = 0
for i in range(2**N):
    switch = f"{i:0{N}b}"
    p_now = [0 for k in range(M)]
    for j in range(N):
        if switch[j] == "1":
            # print(d[j])
            for k in d[j]:
                p_now[k] = (p_now[k] + 1) % 2
    if p_now == p:
        cnt += 1

print(cnt)        
