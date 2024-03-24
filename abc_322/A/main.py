#!/usr/bin/env python3


def solve(N, S):
    for i in range(N-2):
        if S[i] == "A" and S[i+1] == "B" and S[i+2] == "C":
            return i + 1
    return -1


def main():
    N = int(input())
    S = input()
    a = solve(N, S)
    print(a)


if __name__ == '__main__':
    main()
