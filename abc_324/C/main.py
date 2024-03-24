#!/usr/bin/env python3
tmp = list(input().split())
N = int(tmp[0])
T = tmp[1]

ans = []
for i in range(N):
    S = input()
    if len(S) == len(T):
        if T == S:
            ans.append(i+1)
        else:
            cnt = 0
            for j in range(len(T)):
                if S[j] != T[j]:
                    cnt += 1
            if cnt == 1:
                ans.append(i + 1)
    elif len(T)-len(S) == 1:
    # 一文字されてる
        p = 0
        q = 0
        cnt = 0
        while p < len(T) and q < len(S):
            # print(p, q)
            # print(p, q, T[p], S[q])
            if T[p] == S[q]:
                p += 1
                q += 1
            else:
                cnt += 1
                p += 1
        if cnt < 2:
            ans.append(i+1)
    elif len(T)-len(S) == -1:
    # 一文字減っている
        p = 0
        q = 0
        cnt = 0
        while p < len(T) and q < len(S):
            # if i == 5:
            #     print(p, q, T[p], S[q])
            if T[p] == S[q]:
                p += 1
                q += 1
            else:
                cnt += 1
                q += 1
        if cnt < 2:
            ans.append(i+1)
print(len(ans))
print(*ans)

