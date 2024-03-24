#!/usr/bin/env python3
from collections import deque


def solve(N, M, S, T):
    que = deque()
    seen = [0 for i in range(N)]
    for i in range(N-M+1):
        flag = True
        for j in range(M):
            if S[i+j] != T[j] and S[i+j] != "#":
                flag = False
                break
        if flag:
            seen[i] = 1
            que.append(i)
    tmp = list(S)
    rep = ["#"] * M
    # print(que, rep)
    while len(que) > 0:
        i = que.popleft()
        tmp[i:i+M] = rep
        for k in range(max(0, i-M-1), min(i + 2 * (M - 1), N-M+1)):
            if tmp[k:k+M] == rep:
                continue
            flag = True
            for j in range(M):
                # print(tmp[k+j], T[j])
                if tmp[k+j] != T[j] and tmp[k+j] != "#":
                    # print("bad")
                    flag = False
                    break
            # print("===", flag)
            if flag and seen[k] != 1:
                seen[k] = 1
                que.append(k)
        # print(tmp, que)
    if tmp == ["#"] * N:
        return "Yes"
    else:
        return "No"




def main():
    N, M = map(int, input().split())
    S = input()
    T = input()
    a = solve(N, M, S, T)
    print(a)


if __name__ == '__main__':
    main()
