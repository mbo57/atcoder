import heapq

n = int(input())
inq = []
dq = []

for i in range(n):
    t, d = map(int, input().split())
    inq.append((t, t + d))

heapq.heapify(inq)
ans = 0
ls = 0

while inq:
    v = heapq.heappop(inq)
    if not dq:
        ls = max(ls, v[0])
        heapq.heappush(dq, v[1])
    elif v[0] <= ls:
        heapq.heappush(dq, v[1])
    else:
        heapq.heappush(inq, v)
        x = heapq.heappop(dq)
        if x >= ls:
            ans += 1
            ls += 1

while dq:
    x = heapq.heappop(dq)
    if x >= ls:
        ans += 1
        ls += 1

print(ans)
