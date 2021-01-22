#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:59:46 2020

@author: ms
"""

from math import sqrt
N = 5

def periodicity(a):
    if not a:
        return 0
    for i in range(1, len(a) // 2 + 1):
        if all([a[j:j + i] == a[:i] for j in range(0, min(5, len(a) // i), i)]):
            return i
    return 0

def find_periodicity(N):
    a0 = int(sqrt(N))
    tmp = sqrt(N)
    a = []
    step = 0
    while periodicity(a) == 0 or step < 100:
        tmp = 1 / (tmp % 1) 
        a.append(int(tmp))
        step += 1
        # print(a)
        # print(step, periodicity(a))
    return periodicity(a)

# N = int(input())
N = 13
odd = 0
for n in range(N + 1):
    if sqrt(n) % 1 == 0:
        continue
    if find_periodicity(n) % 2 == 1:
        odd += 1
    # print(f'{N:2d}: {find_periodicity(N):2d}')
print(odd)