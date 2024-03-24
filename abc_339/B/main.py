#!/usr/bin/env python3

vec = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solve(H, W, N):
    li = [["." for i in range(W)] for i in range(H)]
    x, y = 0, 0
    v = 0
    for i in range(N):
        # print(x, y)
        if li[x][y] == ".":
            li[x][y] = "#"
            v = (v + 1) % 4
            x = (x + vec[v][0]) % H
            y = (y + vec[v][1]) % W
        else:
            # print("black")
            li[x][y] = "."
            v = (v - 1) % 4
            x = (x + vec[v][0]) % H
            y = (y + vec[v][1]) % W
        # for j in range(H):
        #     print("".join(li[j]))

    return li


def main():
    H, W, N = map(int, input().split())
    a = solve(H, W, N)
    for i in range(H):
        print("".join(a[i]))


if __name__ == '__main__':
    main()
