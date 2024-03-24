#!/usr/bin/env python3


def solve(A, B):
    cnt = 1
    ans = 0
    while cnt < B:
        cnt -= 1
        cnt += A
        ans += 1
    return ans


def main():
    A, B = map(int, input().split())
    a = solve(A, B)
    print(a)


if __name__ == '__main__':
    main()
