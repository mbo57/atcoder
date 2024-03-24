#!/usr/bin/env python3


def solve(S):
    for i in range(1, 16):
        # print(i, S[i], i % 2, S[i])
        if i % 2 == 1 and S[i] == "1":
            return "No"
    return "Yes"


def main():
    S = input()
    a = solve(S)
    print(a)


if __name__ == '__main__':
    main()
