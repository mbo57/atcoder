#!/usr/bin/env python3
import itertools
c = []
for i in range(3):
    c += list(map(int, input().split()))
# print(c)
# print(len(itertools.permutations(c, 9)))
tmp = list(range(9))
cnt = 0

for i in itertools.permutations(tmp, 9):
    # if cnt == 1:
    #     break
    # print(i)
    li = [[] for _ in range(8)]
    for j in i:
        if j == 0:
            li[0].append(c[j])
            li[3].append(c[j])
            li[6].append(c[j])
        if j == 1:
            li[0].append(c[j])
            li[4].append(c[j])
        if j == 2:
            li[0].append(c[j])
            li[5].append(c[j])
            li[7].append(c[j])
        if j == 3:
            li[1].append(c[j])
            li[3].append(c[j])
        if j == 4:
            li[1].append(c[j])
            li[4].append(c[j])
            li[6].append(c[j])
            li[7].append(c[j])
        if j == 5:
            li[1].append(c[j])
            li[5].append(c[j])
        if j == 6:
            li[2].append(c[j])
            li[3].append(c[j])
            li[7].append(c[j])
        if j == 7:
            li[2].append(c[j])
            li[4].append(c[j])
        if j == 8:
            li[2].append(c[j])
            li[5].append(c[j])
            li[6].append(c[j])
    # print(li)
    for j in li:
        if j[0] == j[1]:
            cnt += 1
            break

# print(cnt)
print((362880 - cnt)/362880)
