#!/usr/bin/env python3


def solve(N, K, A):
    lA = len(A)
    As = sorted(A)
    ans = 0
    if lA % 2 == 0:
        for i in range(lA//2):
            ans += As[i * 2 + 1] - As[i * 2]
    else:
        if lA == 1:
            return 0
        lia = [0 for i in range((lA-1)//2)]
        tmpa = 0
        for i in range((lA-1)//2):
            tmpa += As[i * 2 + 1] - As[i * 2]
            lia[i] = tmpa
        lia.insert(0, 0)
        lib = [0 for i in range((lA-1)//2)]
        tmpb = 0
        for i in range((lA-1)//2):
            tmpb += As[-(i * 2 + 1)] - As[-((i + 1) * 2)]
            lib[i] = tmpb
        lib = list(reversed(lib))
        lib.append(0)
        # print(lia)
        # print(lib)
        li = []
        for i in range(lA//2+1):
            li.append(lia[i] + lib[i])
        ans = min(li)

        # ans = min(tmpa, tmpb)
        # for i in range(1, lA):
        #     if i % 2 == 1:
        #         tmp = tmpb + li[i]
            # else:
            #     tmp = tmpb + 

    # tmp = As
    # if lA % 2 == 1:
    #     if As[1] - As[0] > As[-1] - As[-1]:
    #         tmp = As[1:]
    #     else:
    #         tmp = As[:-1]
    # ans = 0
    # for i in range(len(tmp)//2):
    #     ans += tmp[i * 2 + 1] - tmp[i * 2]
    return ans





def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    K = int(next(tokens))
    A = [None for _ in range(K)]
    for i in range(K):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, K, A)
    print(a)


if __name__ == '__main__':
    main()
