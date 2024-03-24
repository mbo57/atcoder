#!/usr/bin/env python3


def solve(S):
    di = {"tourist": 3858,
        "ksun48": 3679,
        "Benq": 3658,
        "Um_nik": 3648,
        "apiad": 3638,
        "Stonefeang": 3630,
        "ecnerwala": 3613,
        "mnbvmar": 3555,
        "newbiedmy": 3516,
        "semiexp": 3481}
    return di[S]


def main():
    S = input()
    a = solve(S)
    print(a)


if __name__ == '__main__':
    main()
