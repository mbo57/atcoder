#!/usr/bin/env python3


def solve(S):
    tmp = S.split("|")
    return tmp[0] + tmp[2]


def main():
    S = input()
    ans = solve(S)
    print(ans)  # TODO: edit here


if __name__ == '__main__':
    main()
