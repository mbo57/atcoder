#!/usr/bin/env python3


def solve(N, M, A):
    ans = [0 for i in range(N)]
    Aso = sorted(A)
    cnt = 1
    s = 0
    e = 0
    while s < N:
        # print(s, e, cnt)
        if Aso[s] <= Aso[e] - M:
            cnt -= 1
            ans[s] = cnt
            s += 1
        else:
            if e == N-1:
                ans[s] = cnt
                cnt -= 1
                s += 1
                # break
            cnt += 1
            e = min(e + 1, N - 1)
    # print(ans)
    return max(ans)


def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    M = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, M, A)
    print(a)


if __name__ == '__main__':
    main()
