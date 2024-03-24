#!/usr/bin/env python3
# from typing import *



# def solve(N: int, M: int, a: List[List[int]]) -> int:
def solve(N, M, a):
    check = [[False for i in range(N)] for i in range(N)]
    for i in range(N):
        check[i][i] = True
    for i in range(M):
        for j in range(N-1):
            tmp1 = a[i][j] - 1
            tmp2 = a[i][j + 1] - 1
            check[tmp1][tmp2] = True
            check[tmp2][tmp1] = True
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not check[i][j]:
                cnt += 1
    return cnt // 2


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    M = int(next(tokens))
    a = [[None for _ in range(N)] for _ in range(M)]
    for j in range(M):
        for i in range(N):
            a[j][i] = int(next(tokens))
    assert next(tokens, None) is None
    a1 = solve(N, M, a)
    print(a1)

if __name__ == '__main__':
    main()
