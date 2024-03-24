#!/usr/bin/env python3
N, M = map(int, input().split())
P = []

for i in range(N):
    P.append(list(map(int, input().split())))

flag = True
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if P[i][0] >= P[j][0]:
            for tmp in P[i][2:]:
                if tmp not in P[j][2:]:
                    flag = False
                    break
            # print(flag)
            if flag and (P[i][0] > P[j][0] or P[i][1] < P[j][1]):
                print("Yes")
                exit(0)
            flag = True
print("No")
