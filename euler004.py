#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 09:07:30 2020

@author: ms
"""

n = 800009

def palin(n):
    a = int(str(n)) - 1
    return int(f'{a:03d}' + f'{a:03d}'[::-1])
def palin_rev(n):
    a = int(str(n)) - 1
    if a < 0:
        return 0
    return int(f'{a:03d}'[::-1] + f'{a:03d}')
def palin_max(n):
    a, b = palin(str(n)[:3]), palin_rev(str(n)[3:])
    if b < 101101:
        return a
    if a < 101101:
        return None
    return max(a,b)
n = palin_max(800000)
print(n)

for i in range(int(str(n)[:3]), 101, -1):
    print(i)