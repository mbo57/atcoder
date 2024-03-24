#!/usr/bin/env python3


def solve(N, S):
    for i in range(N):
        if (S[i] == "a" and S[i-1] == "b") or (S[i] == "b" and S[i-1] == "a"):
            return "Yes"
    return "No"


def main():
    N = int(input())
    S = input()
    a = solve(N, S)
    print(a)


if __name__ == '__main__':
    main()
