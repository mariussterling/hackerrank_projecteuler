#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 19:30:21 2020

@author: ms
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
n = 1
d = 1
res = []
i = 0
while i < N:
    d, n = d + n, n + 2 * d
    i += 1
    if len(str(d)) != len(str(n)):
        print(i)