#!/usr/bin/env python3


def solve(B, G):
    if B > G:
        return "Bat"
    else:
        return "Glove"


def main():
    B, G = map(int, input().split())
    a = solve(B, G)
    print(a)


if __name__ == '__main__':
    main()
