#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 23:51:59 2020

@author: ms
"""

n = 10**10-1
def isPrime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True


from itertools import permutations
base = '123456789'
done = False
l = len(str(n))
for l in range(len(str(n)), 0, -1):
    for i in permutations(base[:l][::-1]):
        i = int(''.join(i))
        if i > n or not isPrime(i):
            continue
        done = True
        break
    if done:
        break
if done:
    print(i)
else:
    print(-1)
    