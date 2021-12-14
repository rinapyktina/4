# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":
    a = list()

    for i in range(10):
        a.append(int(input()))

    biggest = a.index(max(a))
    a[0], a[biggest] = a[biggest], a[0]

    print(a)
