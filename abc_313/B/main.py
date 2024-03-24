#!/usr/bin/env python3


def solve(N, M, A, B):
    li = [1 for i in range(N)]
    for i in range(M):
        li[B[i]-1] = 0
    if sum(li) != 1:
        return -1
    else:
        return li.index(1) + 1


def main():
    N, M = map(int, input().split())
    A = [None for _ in range(M)]
    B = [None for _ in range(M)]
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    a = solve(N, M, A, B)
    print(a)


if __name__ == '__main__':
    main()
