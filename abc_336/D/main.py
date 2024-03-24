#!/usr/bin/env python3


def solve(N, A):
    li = [0 for i in range(N)]
    for i in range(1, N):
        if A[i] == 1:
            li[i] = 0
            continue
        if li[i-1] < A[i] - 1:
            li[i] = li[i-1] + 1
        elif li[i-1] == A[i] - 1:
            li[i] = li[i-1]
        elif li[i-1] == A[i]:
            li[i] = A[i] - 1
    Arev = list(reversed(A))
    lirev = [0 for i in range(N)]
    for i in range(1, N):
        if Arev[i] == 1:
            lirev[i] = 0
            continue
        if lirev[i-1] < Arev[i] - 1:
            lirev[i] = lirev[i-1] + 1
        elif lirev[i-1] == Arev[i] - 1:
            lirev[i] = lirev[i-1]
        elif lirev[i-1] == Arev[i]:
            lirev[i] = Arev[i] - 1
    ans = 0
    lirev = list(reversed(lirev))
    for i in range(N):
        ans = max(min(li[i], lirev[i]), ans)
    # print(li)
    # print(lirev)
    return ans + 1


def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, A)
    print(a)


if __name__ == '__main__':
    main()
