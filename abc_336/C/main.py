#!/usr/bin/env python3


def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)


def solve(N):
    li = [0, 2, 4, 6, 8]
    tmp = base10int(N-1, 5)
    ans = ""
    for i in list(tmp):
        ans += str(li[int(i)])
    # print(tmp)
    return ans


def main():
    N = int(input())
    a = solve(N)
    print(a)


if __name__ == '__main__':
    main()

# 0 2 4 6 8
# 20 22 24 26 28
# 40 42 44 46 48
# 60 62 64 66 68
# 80 82 84 86 88
# 200 202 204 206 208
# 10 5
# 100 25
# 1000 125
# 10000 625
