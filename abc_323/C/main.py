#!/usr/bin/env python3


def solve(N, M, A, S):
    sc = [i + 1 for i in range(N)]
    for i in range(N):
        for j in range(M):
            if S[i][j] == "o":
                sc[i] += A[j]
    maxsc = max(sc)
    li = []
    for i in range(M):
        li.append([A[i], i])
    soA = sorted(li, reverse=True)
    ans = [0 for i in range(N)]
    for i in range(N):
        for j in range(M):
            if sc[i] < maxsc:
                if S[i][soA[j][1]] == "x":
                    sc[i] += soA[j][0]
                    ans[i] += 1
            else:
                break
            # print(i, sc[i])
    return ans


def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    M = int(next(tokens))
    A = [None for _ in range(M)]
    S = [None for _ in range(N)]
    for i in range(M):
        A[i] = int(next(tokens))
    for i in range(N):
        S[i] = next(tokens)
    assert next(tokens, None) is None
    ans = solve(N, M, A, S)
    for i in range(N):
        print(ans[i])


if __name__ == '__main__':
    main()
