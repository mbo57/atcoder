#!/usr/bin/env python3


def solve(S):
    tmp = S
    tmp = tmp.lstrip("A")
    tmp = tmp.lstrip("B")
    tmp = tmp.lstrip("C")
    if len(tmp) == 0:
        return "Yes"
    else:
        return "No"


def main():
    S = input()
    a = solve(S)
    print(a)


if __name__ == '__main__':
    main()
