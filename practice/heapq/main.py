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


test = heapq()
test.push(4)
print(test.li)
test.push(10)
print(test.li)
test.push(13)
print(test.li)
test.push(1)
print(test.li)
test.push(5)
print(test.li)
test.push(2)
print(test.li)
test.push(7)
print(test.li)
test.push(6)
print(test.li)
print(test.toppop())
print(test.li)
print(test.toppop())
print(test.li)
print(test.toppop())
print(test.li)
print(test.toppop())
print(test.li)
print(test.toppop())
print(test.li)
print(test.toppop())
print(test.li)
print(test.toppop())
print(test.li)
print(test.toppop())
print(test.li)
