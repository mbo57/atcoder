#!/usr/bin/env python3
li = []
while True:
    tmp = input()
    li.append(tmp)
    if tmp == "0":
        break
for j in list(reversed(li)):
    print(j)
