#!/usr/bin/env python3


def solve(K, G, M):
    g = 0
    m = 0
    for i in range(K):
        if g == G:
            g = 0
        elif m == 0:
            m = M
        else:
            if G - g >= m:
                g += m
                m = 0
            else:
                m -= G - g
                g = G
    return g, m


def main():
    K, G, M = map(int, input().split())
    c, d = solve(K, G, M)
    print(c, d)


if __name__ == '__main__':
    main()
