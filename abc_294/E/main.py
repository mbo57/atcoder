#!/usr/bin/env python3


def solve(a, b, c, d, e, f, g):


def main():
    a, b, c = map(int, input().split())
    d = [None for _ in range(c)]
    e = [None for _ in range(c)]
    f = [None for _ in range(b)]
    g = [None for _ in range(b)]
    for i in range(c):
        d[i], e[i] = map(int, input().split())
    for i in range(b):
        f[i], g[i] = map(int, input().split())
    a1 = solve(a, b, c, d, e, f, g)
    print(a1)


if __name__ == '__main__':
    main()
