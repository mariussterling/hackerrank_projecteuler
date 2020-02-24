#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 22:26:36 2020

@author: ms
"""
t = int(input())
iis = list(map(int, input().rstrip().split()))

res = [(1, 0), (2, 9)]
for i in range(2, 17):
    res.append((i + 1, res[i - 2][1] + i * 9 * 10 ** (i - 1)))

prod = 1
while iis:
    i = iis.pop()
    d = len(res) - 1
    while res[d][1] > i:
        d -= 1
    tmp = (i - res[d][1]) - 1
    tmp2 = str(10 ** (res[d][0] - 1) + tmp // res[d][0])
    tmp2 = int(tmp2[tmp % res[d][0]])
    prod *= tmp2
    if prod == 0:
        break
print(prod)
