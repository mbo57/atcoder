#!/usr/bin/env python3

class SegmentTree():
    def __init__(self, N: int, func, unit: int = 0):
        self.N = N
        self.X_unit = unit
        self.X = [self.X_unit] * (2*self.N)
        self.X_f = func

    def build(self, seq):
        for i, x in enumerate(seq, self.N):
            self.X[i] = x
        for i in range(self.N - 1, 0, -1):
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def set_val(self, i, x):
        i += self.N
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def fold(self, L, R):
        L += self.N
        R += self.N
        vL = self.X_unit
        vR = self.X_unit
        while L < R:
            if L & 1:
                vL = self.X_f(vL, self.X[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.X_f(self.X[R], vR)
            L >>= 1
            R >>= 1
        return self.X_f(vL, vR)


N, Q = map(int, input().split())
A = list(map(int, input().split()))
query = [list(map(int, input().split())) for _ in range(Q)]


def func(a, b):
    if a[0] > b[0]:
        if a[2] > b[0]:
            return a
        elif a[2] == b[0]:
            return (a[0], a[1], a[2], a[3]+b[1])
        else:
            return (a[0], a[1], b[0], b[1])
    elif a[0] == b[0]:
        if a[2] > b[2]:
            return (a[0], a[1]+b[1], a[2], a[3])
        elif a[2] == b[2]:
            return (a[0], a[1]+b[1], a[2], a[3]+b[3])
        else:
            return (a[0], a[1]+b[1], b[2], b[3])
    else:
        if a[0] > b[2]:
            return (b[0], b[1], a[0], a[1])
        elif a[0] == b[2]:
            return (b[0], b[1], b[2], b[3]+a[1])
        else:
            return b


st = SegmentTree(N, func, (-1, 0, -2, 0))
for i in range(len(A)):
    st.set_val(i, (A[i], 1, -1, 0))

for q in query:
    if q[0] == 1:
        st.set_val(q[1]-1, (q[2], 1, -1, 0))
    else:
        print(st.fold(q[1]-1, q[2])[3])
