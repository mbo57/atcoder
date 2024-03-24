#!/usr/bin/env python3
import itertools
N = int(input())
S = input()

tmp = "ABXY"
di = {}
ans = 10 ** 10
for tmp1, tmp2 in itertools.product(tmp, repeat=2):
    Stmp = S
    key1 = tmp1 + tmp2
    Stmp = Stmp.replace(key1, "L")
    for tmp1, tmp2 in itertools.product(tmp, repeat=2):
        key2 = tmp1 + tmp2
        Stmp1 = Stmp.replace(key2, "R")
        ans = min(len(Stmp1), ans)
print(ans)
