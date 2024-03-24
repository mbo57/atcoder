#!/usr/bin/env python3


def solve(S):
    li = list(S.split("."))
    return li[-1]


def main():
    S = input()
    a = solve(S)
    print(a)


if __name__ == '__main__':
    main()
