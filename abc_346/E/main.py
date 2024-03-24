#!/usr/bin/env python3


def solve(H, W, M, T, A, X):
    h = set([i for i in range(H)])
    w = set([i for i in range(W)])
    di = {0: 0}
    for i in range(M):
        di[X[i]] = 0
    # print(w, h)
    for i in range(M)[::-1]:
        if T[i] == 1:
            if A[i]-1 in h:
                di[X[i]] += len(w)
                h.remove(A[i]-1)
        else:
            if A[i]-1 in w:
                di[X[i]] += len(h)
                w.remove(A[i]-1)
        # print(T[i], A[i]-1, X[i], w, h)
    tmp = sum(list(di.values())) - di[0]
    di[0] = H * W - tmp
    score_sorted = sorted(di.items(), key=lambda x: x[0])
    a = []
    b = []
    for key, val in score_sorted:
        if val != 0:
            a.append(key)
            b.append(val)
    # print(di)
    return len(a), a, b


def main():
    H, W, M = map(int, input().split())
    T = [None for _ in range(M)]
    A = [None for _ in range(M)]
    X = [None for _ in range(M)]
    for i in range(M):
        T[i], A[i], X[i] = map(int, input().split())
    n, a, b = solve(H, W, M, T, A, X)
    print(n)
    for i in range(n):
        print(a[i], b[i])


if __name__ == '__main__':
    main()
