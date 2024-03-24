#!/usr/bin/env python3


def solve(N, X, Y):
    a = sum(X)
    b = sum(Y)
    if a == b:
        return "Draw"
    elif a > b:
        return "Takahashi"
    else:
        return "Aoki"



def main():
    N = int(input())
    X = [None for _ in range(N)]
    Y = [None for _ in range(N)]
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    a = solve(N, X, Y)
    print(a)


if __name__ == '__main__':
    main()
