#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 18:23:06 2020

@author: ms
"""

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

p = primes(10**9)
with open('primes.txt', 'w') as f:
    f.write(', '.join(map(str, p)))
from itertools import dropwhile
from math import log10

res = {i: 0 for i in range(int(log10(p[-1])) + 2)}
for i in p:
    res[int(log10(i)) + 1] += 1
{k: round(v / (9*10**(k-1))*100,2) for k, v in res.items()}
