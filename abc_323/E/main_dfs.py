#!/usr/bin/env python3
import sys
import collections
sys.setrecursionlimit(10 ** 6)

li = []


def dfs(t, num, X, T, N):
    global li
    for i in range(N):
        if t + T[i] < X + 0.5:
            dfs(t + T[i], num + 1, X, T, N)
        else:
            if i == 0:
                li.append(num)


def find_unique_z(x, y, m):
    # 逆元を計算
    x_inv = pow(x, m - 2, m)
    # z = y * x_inv (mod m) で解を計算
    z = (y * x_inv) % m
    return z


def solve(N, X, T):
    global li
    dfs(0, 1, X, T, N)
    # print(li)
    maxli = max(li)
    y = 0
    c = collections.Counter(li)
    for tmp in list(c.items()):
        y += (N ** (maxli - tmp[0])) * tmp[1]
    x = N ** maxli
    # print(y, x)
    return find_unique_z(x, y, 998244353)


def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    X = int(next(tokens))
    T = [None for _ in range(N)]
    for i in range(N):
        T[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, X, T)
    print(a)


if __name__ == '__main__':
    main()
