#!/usr/bin/env python3


def solve(N, S):
    cnt = 0
    b = ""
    di = {}
    for i in range(N):
        # print(S[i])
        if b == S[i]:
            cnt += 1
        else:
            cnt = 1
        if S[i] in di:
            di[S[i]] = max(di[S[i]], cnt)
        else:
            di[S[i]] = cnt
        b = S[i]
    # print(di)
    return sum(di.values())




def main():
    N = int(input())
    S = input()
    a = solve(N, S)
    print(a)


if __name__ == '__main__':
    main()
