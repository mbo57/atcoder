#!/usr/bin/env python3


def solve(N, T, M, A, B):
    


def main():
    N, T, M = map(int, input().split())
    A = [None for _ in range(M)]
    B = [None for _ in range(M)]
    for i in range(M):
        A[i], B[i] = input().split()
    a = solve(N, T, M, A, B)
    print(a)


if __name__ == '__main__':
    main()
