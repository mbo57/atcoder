#!/usr/bin/env python3
import copy


def rotite(a):
    # for i in range(n):
    tmp = ""
    for ind, x in enumerate(zip(*a[::-1])):
        a[ind] = list(x)
        tmp += "".join(x)
    return tmp


def move(a, N, M):
    tmp = "...." * N
    for i in range(4-N):
        tmp += "." * M + "".join(a[i][:4-M])
    return tmp


def printmy(a):
    for i in range(4):
        print(a[i*4:(i+1)*4])
    print("====")


def remove(a):
    cnt = 0
    for i in range(4):
        if a[i] == ["." for i in range(4)]:
            cnt += 1
        else:
            break
    tmp = a[cnt:] + [["." for i in range(4)] for i in range(cnt)]
    # print(tmp)
    cnt = 0
    for ind, x in enumerate(zip(*tmp[::-1])):
        # print(x == (".", ".", ".", "."))
        if x == (".", ".", ".", "."):
            cnt += 1
        else:
            break
    for i in range(4):
        tmp[i] = tmp[i][cnt:] + ["." for _ in range(cnt)]
    return tmp


P = [[] for i in range(3)]
for i in range(3):
    for j in range(4):
        tmp = list(input())
        P[i].append(tmp)


tmp = [[0 for i in range(4)] for i in range(4)]


p0_cnt = 0
p1_cnt = 0
p2_cnt = 0
for i in range(4):
    p0_cnt += P[0][i].count("#")
    p1_cnt += P[1][i].count("#")
    p2_cnt += P[2][i].count("#")

for r0 in range(4):
    rotite(P[0])
    p0 = remove(P[0])
    for i0 in range(4):
        for j0 in range(4):
            a = move(p0, i0, j0)
            if a.count("#") != p0_cnt:
                continue

            for r1 in range(4):
                rotite(P[1])
                p1 = remove(P[1])
                for i1 in range(4):
                    for j1 in range(4):
                        b = move(p1, i1, j1)
                        if b.count("#") != p1_cnt:
                            continue

                        for r2 in range(4):
                            rotite(P[2])
                            p2 = remove(P[2])
                            for i2 in range(4):
                                for j2 in range(4):
                                    c = move(p2, i2, j2)
                                    if c.count("#") != p2_cnt:
                                        continue
                                    tmp = ["." for i in range(16)]
                                    for i in range(16):
                                        cnt = 0
                                        if a[i] == "#":
                                            cnt += 1
                                        if b[i] == "#":
                                            cnt += 1
                                        if c[i] == "#":
                                            cnt += 1
                                        if cnt == 1:
                                            tmp[i] = "#"
                                        # print(tmp)
                                        if "." not in tmp:
                                            # print(p0, i0, j0, a)
                                            # print(p1, i1, j1, b)
                                            # print(p2, i2, j2, c)
                                            print("Yes")
                                            exit(0)
                                    # if r0 == 0 and i0 == 1 and j0 == 0 and
print("No")

