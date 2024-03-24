#!/usr/bin/env python3


def solve(N, S):
    a = False
    b = False
    c = False
    for i in range(N):
        if S[i] == "A":
            a = True
        if S[i] == "B":
            b = True
        if S[i] == "C":
            c = True
        if a and b and c:
            return i + 1


def main():
    N = int(input())
    S = input()
    a = solve(N, S)
    print(a)


if __name__ == '__main__':
    main()
