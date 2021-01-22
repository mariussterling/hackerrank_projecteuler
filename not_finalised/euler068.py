#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 22:11:50 2020

@author: ms
"""

from itertools import permutations

def solution(i):
    x = [[None, None] for _ in range(n)]
    s = set(s0)
    si = si0
    so = so0
    if si - sum(i) < 1:
        return None
    for j, l in enumerate(i):
        x[j - 1][1] = l
        si -= l
        s.remove(l)

    x[0][0] = tmp = c - x[0][1] - x[1][1]
    so -= tmp
    if tmp not in s or so < 1:
        return None
    s.remove(tmp)

    for j in range(1, n):
        if x[j][1] is None:
            x[j][1] = tmp = c - x[j - 1][1] - x[j - 1][0]
            si -= tmp
            if tmp not in s or si < 1:
                return None
            s.remove(tmp)
        if x[j][0] is None:
            x[j][0] = tmp = x[j - 1][0] - x[j][1] + x[j - 2][1]
            so -= tmp
            if tmp not in s or so < 1:
                return None
            s.remove(tmp)
        
    return x


n = 3
c = 12

si0 = n * c - n * (2 * n + 1)
so0 = 2 * n * (2 * n + 1) - n * c

# m1 = min(2 * n, si - n * (n + 1) // 2)
# m0 = max(1, si - n * (2 * n + 1))
# print(m0, m1)
s0 = set(i for i in range(1, 2 * n + 1))
for i in permutations(range(1, 2 * n + 1), 3):
    tmp = solution(i)
    if tmp is None:
        continue
    print(solution(i))
