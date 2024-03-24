#!/usr/bin/env python3


def solve(X, Y):
    if -3 <= Y - X <= 2:
        return "Yes"
    return "No"


def main():
    X, Y = map(int, input().split())
    a = solve(X, Y)
    print(a)


if __name__ == '__main__':
    main()
