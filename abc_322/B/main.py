#!/usr/bin/env python3


def solve(N, M, S, T):
    before = False
    after = False
    if S == T[:N]:
        before = True
    if S == T[-N:]:
        after = True
    # print(before, after)

    if after and before:
        return 0
    elif before and not after:
        return 1
    elif not before and after:
        return 2
    else:
        return 3


def main():
    N, M = map(int, input().split())
    S = input()
    T = input()
    a = solve(N, M, S, T)
    print(a)


if __name__ == '__main__':
    main()
