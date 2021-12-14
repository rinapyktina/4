# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":
    a = list(map(float, input().split()))

    s = 0

    for i in range(len(a)):
        if i % 2 == 1:
            s += a[i]

    n = list()
    for i in a:
        if i < 0:
            n.append(i)

    first = a.index(n[0])
    last = a.index(n[-1])

    b = sum(a[first:last]) - n[0]

    for i in range(len(a)):
        if abs(a[i]) <= 1:
            a[i] = 0

    print(s)
    print(b)
    print(a)
