#!/usr/bin/env python3


def solve(S):
    ans = ""
    cnt = 0
    i = 0
    b = 1
    c = 2
    # for i in range(len(S)):
    while i < len(S):
        ans += S[i]
        # print(ans, ans[-3:])
        if ans[-3:] == "ABC":
            ans = ans[:-3]
            # print("aaa", ans)
        i += 1
    return ans


    # a = len(S)
    # tmp = S
    # while True:
    #     tmp = tmp.replace("ABC", "")
    #     b = len(tmp)
    #     if a == b:
    #         break
    #     a = b
    # return tmp


def main():
    S = input()
    ans = solve(S)
    print(ans)  # TODO: edit here


if __name__ == '__main__':
    main()
