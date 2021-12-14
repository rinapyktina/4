# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":
    lst = list(map(float, input().split()))
    a = float(input())
    b = float(input())

    print(max(lst))

    n = list()
    for i in lst:
        if i > 0:
            n.append(i)

    last = lst.index(n[-1])

    s = sum(lst[:last])
    print(s)

    for i in range(len(lst)):
        if a <= abs(lst[i]) <= b:
            lst[i] = 0

    print(lst)
