#!/usr/bin/env python3
N = int(input()) - 1

tmp = bin(N)[2:]
M = len(tmp)
print(M)
li = [[] for i in range(M)]
for i in range(N+1):
    tmp = (bin(i)[2:]).zfill(M)
    # print(i+1, "本目", tmp)
    for j in range(M):
        if tmp[j] == "1":
            li[j].append(i+1)
for i in range(M):
    # print(i+1, "人目", li[i])
    print(len(li[i]), *li[i])
S = input()
print(int(S, 2)+1)
exit(0)
