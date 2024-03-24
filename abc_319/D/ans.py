n, m = map(int, input().split())

L = list(map(int, input().split()))

sort_L = sorted(L)
lower = sort_L.pop(-1)
upper = sum(L) + len(L)-1

if m == 1:
    ans = upper
else:
    ans = lower
    while lower < upper:
        middle = (lower + upper) // 2
        lines = 1
        tmp = 0
        for l in L:
            if tmp + l > middle:
                lines += 1
                tmp = l + 1
            else:
                tmp +=  l + 1
            if lines > m:
                break
        if lines > m:
            lower = middle + 1
        else:
            upper = middle
        # print(lower, middle, upper, lines)
    ans = lower


print(ans)
