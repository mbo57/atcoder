#!/usr/bin/env python3


def solve(N):
    ans = 1
    i = 1
    while i ** 3 <= N:
        tmp = i ** 3
        tmps = str(tmp)
        num = len(tmps) // 2
        # print(tmp, tmps[:num], ''.join(list(reversed(tmps[-num:]))), i)
        if tmps == tmps[::-1]:
            ans = tmp
        i += 1
    # print(i)
    return ans


def main():
    N = int(input())
    a = solve(N)
    print(a)


if __name__ == '__main__':
    main()
