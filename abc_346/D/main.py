#!/usr/bin/env python3


def solve(N, S, C):
    sint = int(S, 2)
    c = "1" + "10" * (N // 2)
    tmp = int(c[:N], 2)

    a = sint ^ tmp
    a = '{:0{b}b}'.format(a, b=N)

    # print(S)
    # print(c[:N])
    # print(a)
    mcost = sum(C)
    cost = 0
    for i in range(len(a)):
        if a[i] == "1":
            cost += C[i]
    scost = cost
    ans = min(mcost - cost, cost)
    # print("aaa", mcost, scost)
    for i in range(1, N-1):
        if a[i] == "1":
            cost = scost - C[i]
        else:
            cost = scost + C[i]
        scost = cost
        ans = min(mcost - cost, cost, ans)
        # print(i, cost, scost, ans)
    # print(cost)
    # print(int("10", 2))
    return ans


def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    C = [None for _ in range(N)]
    S = next(tokens)
    for i in range(N):
        C[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, S, C)
    print(a)


if __name__ == '__main__':
    main()
