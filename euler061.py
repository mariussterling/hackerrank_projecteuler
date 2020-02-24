#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 17:17:13 2020

@author: ms
"""

from math import sqrt, ceil, floor
def n(x, k):
    res = (k - 4) / (k - 2)
    return 1 / 2 * res + sqrt(1 / 4 * res ** 2 + 2 * x / (k - 2))
def p(i, k):
    return int(i * (i * (k / 2 - 1) + 2 - k /2))

def find_next(res):
    x = res[-1][1] % 100
    Ns = res[-1][2]
    poss = []
    for k in Ns:
        m1 = ceil(n(x * 100, k))
        m2 = floor(n(x * 100 + 100, k)) + 1
        for i in range(m1, m2):
            if x % 100 // 10 == 0:
                continue
            if p(i, k) % 1 == 0:
                tmp = [[k, p(i, k), set([i for i in Ns if k != i])]]
                if tmp[-1][2]:
                    tmp2 = find_next(res + tmp)
                    if tmp2 is not None:
                        poss.extend(tmp2)
                else:
                    poss.append(res + tmp)
    poss = [p for p in poss if p is not None]
    if not poss:
        return None
    else:
        return poss
# t = int(input())
Ns = list(map(int, '3 4 5 6 7'.rstrip().split()))
k = min(Ns)
Ns.remove(k)
res2 = []
for i in range(ceil(n(1011, k)), floor(n(9999, k)) + 1):
    x = p(i, k)
    if x % 100 // 10 == 0:
        continue
    res = [[k, x, set(i for i in Ns if k != i)]]
    res = find_next(res)
    if res is None:
        continue
    for i in res:
        if i[0][1] // 100 != i[-1][1] % 100:
            continue
        if len(set([j[1] for j in i])) != len(i):
            continue
        if sorted(set([j[1] for j in i])) not in res2:
            res2.append(sorted(set([j[1] for j in i])))
for i in sorted([sum(i) for i in res2]):
    print(i)


