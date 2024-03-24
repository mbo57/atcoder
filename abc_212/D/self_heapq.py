#!/usr/bin/env python3
class heapq():
    def __init__(self):
        self.li = []

    def push(self, num):
        self.li.append(num)
        childlen = len(self.li) - 1
        parent = childlen
        while parent != 0:
            parent = (childlen - 1) // 2
            if num < self.li[parent]:
                tmp = self.li[parent]
                self.li[parent] = num
                self.li[childlen] = tmp
                childlen = parent
            else:
                break

    def toppop(self):
        popval = self.li[0]
        tmp = self.li.pop()
        length = len(self.li)
        if length == 0:
            return popval
        self.li[0] = tmp
        parent = 0
        while parent < length:
            childlen1 = parent * 2 + 1
            childlen2 = parent * 2 + 2
            if childlen1 >= length:
                break
            elif childlen2 >= length:
                childlen = childlen1
            elif self.li[childlen1] < self.li[childlen2]:
                childlen = childlen1
            else:
                childlen = childlen2
            if self.li[childlen] < self.li[parent]:
                tmp = self.li[parent]
                self.li[parent] = self.li[childlen]
                self.li[childlen] = tmp
                parent = childlen
            else:
                break
        return popval


Q = int(input())

heapq = heapq()
add = 0
for i in range(Q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        heapq.push(que[1] - add)
    elif que[0] == 2:
        add += que[1]
    elif que[0] == 3:
        tmp = heapq.toppop()
        print(tmp + add)
