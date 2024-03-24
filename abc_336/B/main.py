#!/usr/bin/env python3


def solve(N):
    tmp = bin(N)[2:]
    # print(tmp[2:])
    cnt = 0
    for i in list(reversed(tmp)):
        # print(i)
        if i == "0":
            cnt += 1
        else:
            break
    return cnt


def main():
    N = int(input())
    a = solve(N)
    print(a)


if __name__ == '__main__':
    main()
