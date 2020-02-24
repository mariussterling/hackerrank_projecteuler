#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 00:26:23 2020

@author: ms
"""
from math import sqrt

n, k = map(int, input().rstrip().split())
def pentagonal(n):
    return n * (3 * n - 1) // 2

for i in range(k + 1, n + 1):
    p0 = pentagonal(i)
    p1 = pentagonal(i - k)
    x0 = sqrt(1 + 24 * (p0 - p1))
    x1 = sqrt(1 + 24 * (p0 + p1))
    if x0 % 6 == 5 or x1 % 6 == 5:
        print(p0)

