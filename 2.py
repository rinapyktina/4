# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":
    a = list()

    for i in range(10):
        a.append(int(input()))

    n = 1

    for i in a:
        if i > 0:
            n *= i

    print(n)
