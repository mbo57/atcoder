#!/usr/bin/env python3
# from typing import *


# def solve(N: int, S: str) -> Any:
def solve(N, S):
    ans = [0 for i in range(N)]
    tmpS = list(S)
    for i in range(N):
        if S[i] == ")":
            j = i
            while tmpS[j] != "(" and j != -1:
                j -= 1
            if j == -1:
                continue
            tmpS[j] = "."
            print(j, i)
            ans[j:i+1] = [1 for _ in range(i-j+1)]
            # print(ans)
    tmp = ""
    for i in range(N):
        if ans[i] == 0:
            tmp += S[i]
    return tmp

    # li_r = {}
    # li_l = {}
    # tmpi = 0
    # tmpj = 0
    # for i in range(N):
    #     if S[i] == "(":
    #         li_l[tmpi] = i
    #         tmpi += 1
    #     elif S[i] == ")":
    #         li_r[tmpj] = i
    #         tmpj += 1
    # # max_len = max(len(li_r), len(li_l))
    # # print(li_l)
    # i = 0
    # j = 0
    # ans = [0 for i in range(N)]
    # while len(li_l) > i and len(li_r) > j:
    #     # print(i, j)
    #     if li_l[i] > li_r[j]:
    #         j += 1
    #     else:
    #         if i+1 == len(li_l) or li_l[i+1] > li_r[j]:
    #             # tmpa = li_l[i+1]
    #             # tmpb = 
    #             a = li_l.pop(i)
    #             b = li_r.pop(j)
    #             ans[a:b+1] = [1 for i in range(b-a+1)]
    #             print(ans)
    #             i -= 1
    #         else:
    #             i += 1
    # tmp = ""
    # for i in range(N):
    #     if ans[i] == 0:
    #         tmp += S[i]
    # return tmp


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    S = input()
    ans = solve(N, S)
    print(ans)  # TODO: edit here


if __name__ == '__main__':
    main()