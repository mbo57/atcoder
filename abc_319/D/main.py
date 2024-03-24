#!/usr/bin/env python3


def check(N, M, L, W):
    length = L[0]
    cnt = 1
    for i in range(1, N):
        if length + L[i] + 1 <= W:
            length += L[i] + 1
        else:
            cnt += 1
            length = L[i]
        if cnt > M:
            return cnt
    return cnt


def solve(N, M, L):
    # print(check(N, M, L, 8))
    # print(check(N, M, L, 9))
    # print(check(N, M, L, 10))
    l = max(L)
    # print(l)
    if check(N, M, L, l) <= M:
        return l
    r = sum(L) + N - 1
    while r - l > 1:
        m = (r + l) // 2
        tmp = check(N, M, L, m)
        # print(l, m, r, tmp)
        if tmp > M:
            l = m
        else:
            r = m
        # print(l, m, r, tmp, check(N, M, L, l))
    # print("aa", M)
    return r



def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    M = int(next(tokens))
    L = [None for _ in range(N)]
    for i in range(N):
        L[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, M, L)
    print(a)


if __name__ == '__main__':
    main()
