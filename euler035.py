#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 01:47:31 2020

@author: ms
"""


def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    # return [2] + [i for i in range(3, n, 2) if sieve[i]]
    return [i for i in range(n - 1, 2, -2) if sieve[i]] + [2]

prim = primes(100)
res = 0
for i in prim:
    if all([int(str(i)[j:] + str(i)[:j]) in prim for j in range(1,len(str(i)))]):
        res += i
res



#
res = 0
while prim:
    p = prim.pop()
    if p <= 10:
        res += p
        continue
    else:
        break
while prim:
    p = prim.pop()
    tmp = [int(str(p)[j:] + str(p)[:j]) for j in range(1, len(str(p)) + 1) 
           if int(str(p)[j:] + str(p)[:j]) in prim]
    if len(tmp) == len(str(p)) - 1:
        res += sum(tmp) + p
    for p in tmp:
        prim.pop(p)
res
    
for i in prim:
    for j in range(1, len(str(i))):
        if int(str(i)[j:] + str(i)[:j]) not in prim:
            break
    res += i
print(res)
