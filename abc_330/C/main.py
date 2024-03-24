#!/usr/bin/env python3


def solve(D):
    for x in range(1414215):
        if x ** 2 > D:
            tmp = D - x ** 2
            break
    mi = abs(tmp)
    tmpx = x
    tmpy = 0
    while tmpx >= tmpy:
        before = 10 ** 10
        while tmpx >= tmpy:
            tmp = abs(tmpx ** 2 + tmpy ** 2 - D)
            mi = min(tmp, mi)
            if tmp > before:
                tmpy -= 1
                break
            before = tmp
            tmpy += 1
        tmpx -= 1
    return mi




def main():
    D = int(input())
    a = solve(D)
    print(a)


if __name__ == '__main__':
    main()
