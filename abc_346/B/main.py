#!/usr/bin/env python3


def solve(W, B):
    s = "wbwbwwbwbwbw" * 250
    for i in range(len(s)-B-W):
        # print(s[i:i+W+B])
        w = s[i:i+W+B].count("w")
        b = s[i:i+W+B].count("b")
        if w == W and b == B:
            return "Yes"
    return "No"


def main():
    W, B = map(int, input().split())
    a = solve(W, B)
    print(a)


if __name__ == '__main__':
    main()
