#!/usr/bin/env python3
A = []
for i in range(9):
    A.append(list(map(int, input().split())))


AT = list(zip(*A))

for i in range(9):
    if len(set(A[i])) != 9 or len(set(AT[i])) != 9:
        print("No")
        exit(0)
for i in range(3):
    for j in range(3):
        li = []
        for p in range(3):
            for q in range(3):
                a = (i * 3) + p
                b = (j * 3) + q
                li.append(A[a][b])
                # print(a, b)
        # print(li)
        if len(set(li)) != 9:
            print("No")
            exit(0)
print("Yes")
