#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 18:30:00 2020

@author: ms
"""

from math import sqrt
from itertools import combinations
from functools import reduce


def prod(l):
    return reduce((lambda x, y: x * y), l)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def primeFactors(n):
    res = []
    while n % 2 == 0:
        res.append(2)
        n = n // 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            res.append(i)
            n = n // i
    if n > 2:
        res.append(n)
    return set(res)
n = 210
def phi2(n):
    return sum([1 for i in range(n) if gcd(n, i) == 1])


def phi(n):
    m = 0
    s = primeFactors(n)
    for i in range(len(s)):
        m += (-1) ** i * sum([n // prod(j) for
                              j in combinations(s, i + 1)])
    return n - m


for n in range(100, 211, 1):
    a = phi(n)
    b = phi2(n)
    print(f'{n:3d}: {a == b}, {a}, {b}, {a-b}')
