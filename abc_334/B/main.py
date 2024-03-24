#!/usr/bin/env python3


def solve(A, M, L, R):
    cnt = (R - L) // M
    print(cnt, (L-A) % M, (R-A) % M)
    if (L - A) % M == 0:
        cnt += 1
    if (R - A) % M == 0:
        cnt += 1
    return cnt


def main():
    A, M, L, R = map(int, input().split())
    a = solve(A, M, L, R)
    print(a)


if __name__ == '__main__':
    main()
