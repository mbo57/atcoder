#!/usr/bin/env python3


def solve(N, A):
    di = {}
    for i in range(N):
        di[A[i]] = i + 1
    tmp = -1
    ans = []
    for i in range(N):
        # print(tmp, ans)
        ans.append(di[tmp])
        tmp = di[tmp]
    # print(ans)
    return ans


def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    ans = solve(N, A)
    print(*[ans[i] for i in range(N)])


if __name__ == '__main__':
    main()
