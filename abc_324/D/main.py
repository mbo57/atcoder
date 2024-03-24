#!/usr/bin/env python3
import collections


def solve(N, S):
    scounter = collections.Counter(list(S))
    ans = 0
    for i in range(10000000):
        if i * i > int("9"*N):
            break
        tmp = f"{i*i:0{N}d}"
        tmpcounter = collections.Counter(list(tmp))
        if scounter == tmpcounter:
            ans += 1
    return ans


def main():
    N = int(input())
    S = input()
    a = solve(N, S)
    print(a)


if __name__ == '__main__':
    main()
