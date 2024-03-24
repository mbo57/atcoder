#!/usr/bin/env python3
import math


def solve(N, M, K):
    same = N * M // math.gcd(N, M)
    num = same//N + same//M - 2
    tmp = K // num
    mod = K % num
    if mod == 0:
        tmp -= 1
        mod = num
    a = N
    b = M
    i = 0
    j = 1
    if a > b:
        a, b = b, a
    cnt = 0
    while cnt < mod:
        kk = b // a
        if kk + cnt >= mod:
            kk = mod - cnt
        i += kk
        cnt += kk
        ans = a * i
        # print(cnt, ans, i, kk)
        if cnt < mod:
            ans = b * j
            cnt += 1
            j += 1
        # print(cnt, ans)

    # print("tmp", "mod", "same", "ans")
    # print(tmp, mod, same, ans, num)
    # print(ans, "+", same, "*", tmp)
    return ans + same * tmp


def main():
    N, M, K = map(int, input().split())
    a = solve(N, M, K)
    print(a)


if __name__ == '__main__':
    main()
