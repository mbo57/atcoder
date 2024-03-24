#!/usr/bin/env python3


def solve(N, D):
    cnt = 0
    for i in range(1, N+1):
        for day in range(1, D[i-1]+1):
            tmp = str(i) + str(day)
            li = list(tmp)
            a = set(li)
            if len(a) == 1:
                # print(i, day)
                cnt += 1
    return cnt





def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    D = [None for _ in range(N)]
    for i in range(N):
        D[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, D)
    print(a)


if __name__ == '__main__':
    main()
