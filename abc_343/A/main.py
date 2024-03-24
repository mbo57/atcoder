#!/usr/bin/env python3


def solve(A, B):
    for i in range(10):
        if A + B != i:
            return i


def main():
    A, B = map(int, input().split())
    a = solve(A, B)
    print(a)


if __name__ == '__main__':
    main()
