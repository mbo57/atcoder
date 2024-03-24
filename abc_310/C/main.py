#!/usr/bin/env python3


def solve(N, S):
    se = set()
    ans = 0
    for i in range(N):
        if S[i] not in se and S[i][::-1] not in se:
            ans += 1
            se.add(S[i])
    # print(se)
    return ans


def main():
    N = int(input())
    S = [None for _ in range(N)]
    for i in range(N):
        S[i] = input()
    a = solve(N, S)
    print(a)


if __name__ == '__main__':
    main()
