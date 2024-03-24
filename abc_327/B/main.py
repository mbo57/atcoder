#!/usr/bin/env python3


def solve(B):
    tmp = 0
    i = 1
    while tmp < B:
        tmp = i ** i
        if tmp == B:
            return i
        i += 1
    return -1


def main():
    B = int(input())
    a = solve(B)
    print(a)


if __name__ == '__main__':
    main()
