#!/usr/bin/env python3


def solve(N):
    div = make_divisors(N)
    # print(div)
    ans = ""
    for i in range(N+1):
        li = []
        for j in div:
            if i % (N//j) == 0:
                li.append(j)
        # print(i, li)
        if len(li) == 0:
            ans += "-"
        else:
            ans += str(min(li))
    return ans


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            if i <= 9:
                lower_divisors.append(i)
            if i != n // i:
                if n//i <= 9:
                    upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def main():
    N = int(input())
    a = solve(N)
    print(a)


if __name__ == '__main__':
    main()
