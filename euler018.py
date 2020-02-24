#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:16:14 2020

@author: ms
"""

from itertools import product

ar = [[3],[7,4],[2,4,6],[8,5,9,3]]
m = 0
for drct in product([0, 1], repeat=len(ar)-1):
    d = [0]+[sum(drct[:i+1]) for i, x in enumerate(drct)]    
    t = sum([ar[l][idx] for l, idx in enumerate(d)])
    print(d, t)
    m = max(m, t)
print(m)