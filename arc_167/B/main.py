#!/usr/bin/env python3
mod = 998244353

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


def solve(A, B):
    tmp = factorization(A)
    di = {}
    allnum = 1
    for i in range(len(tmp)):
        allnum *= (B * tmp[i][1]) + 1
    for i in range(len(tmp)):
        a = tmp[i][1] * B
        num = (a * (a + 1) // 2) * (allnum // ((B * tmp[i][1]) + 1))
        di[tmp[i][0]] = num // tmp[i][1]
    return max(di.values()) % mod


def main():
    A, B = map(int, input().split())
    a = solve(A, B)
    print(a)


if __name__ == '__main__':
    main()
