#!/usr/bin/env python3


def solve(N, T, A, B):
    di = {}
    di[0] = N
    sco = [0 for i in range(N)]
    cnt = 1
    ans = [0 for i in range(T)]
    for i in range(T):
        # print(di)
        tmp = A[i] - 1
        # print(sco[tmp])
        di[sco[tmp]] -= 1
        if di[sco[tmp]] == 0:
            cnt -= 1
        sco[tmp] += B[i]
        if sco[tmp] in di:
            if di[sco[tmp]] == 0:
                cnt += 1
            di[sco[tmp]] += 1
        else:
            di[sco[tmp]] = 1
            cnt += 1
        # print(cnt)
        ans[i] = cnt
    return ans


def main():
    N, T = map(int, input().split())
    A = [None for _ in range(T)]
    B = [None for _ in range(T)]
    for i in range(T):
        A[i], B[i] = map(int, input().split())
    ans = solve(N, T, A, B)
    for i in range(T):
        print(ans[i])


if __name__ == '__main__':
    main()
