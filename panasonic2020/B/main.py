#!/usr/bin/env python3


def solve(H, W):
    if H == 1 or W == 1:
        return 1
    w1 = W // 2
    w2 = w1
    if W % 2 == 1:
        w1 += 1
    ans = (w1 + w2) * (H // 2)
    if H % 2 == 1:
        ans += w1
    # print(H // 2)
    # print(w1, w2, H % 2)
    return ans


def main():
    H, W = map(int, input().split())
    a = solve(H, W)
    print(a)


if __name__ == '__main__':
    main()
