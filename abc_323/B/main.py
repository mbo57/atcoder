#!/usr/bin/env python3


def solve(N, S):
    sc = [[0, i] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == "x":
                sc[i][0] += 1
    sc.sort()
    ans = []
    for i in range(N):
        ans.append(sc[i][1]+1)
    return ans


def main():
    N = int(input())
    S = [None for _ in range(N)]
    for i in range(N):
        S[i] = input()
    ans = solve(N, S)
    print(*[ans[i] for i in range(N)])


if __name__ == '__main__':
    main()
