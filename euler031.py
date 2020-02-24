#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 00:02:06 2020

@author: ms
"""

n = 9
# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations as perm
n = int(input())
for n in range(4, 10):
    d = {4: [(2, 1, 1)],
         5: [(2, 1, 2)],
         6: [(3, 1, 2)],
         7: [(3, 2, 2), (3, 1, 3)],
         8: [(4, 1, 3), (4, 2, 2)],
         9: [(4, 1, 4), (4, 2, 3)]}
    poss = [str(i) for i in range(1, n + 1)]
    res = []
    for x in d[n]:
        for p0 in perm(poss, n):
            p = int(''.join(p0[:x[0]]))
            a = int(''.join(p0[x[0]:x[0] + x[1]]))
            b = int(''.join(p0[x[0] + x[1]:]))
            if x[1] == x[2] and a > b:
                continue
            if p != a * b:
                continue
            res.append((min(a, b), max(a, b), p))
            res.append((max(a, b), min(a, b), p))
            # res.update((min(a, b), max(a, b), p))
            # print(a,b,p)
    
    res = set(res)
    s = sum([i[2] for i in res])
    print(s)
    # print(f'{n}: {sum([i[2] for i in res])}')
if res:
    print(sum([i[2] for i in res]))
else:
    print(0)