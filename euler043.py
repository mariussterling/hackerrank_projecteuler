#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 22:47:27 2020

@author: ms
"""

from itertools import permutations
numbers = '0123456789'
for n in range(3, 10):
    res = 0
    for p in permutations(numbers[:n + 1]):
        if n >= 5 and p[5] not in ['0', '5']:
            continue
        if p[3] not in ['0', '2', '4', '6', '8']:
            continue
        if n >= 9 and int(p[7] + p[8] + p[9]) % 17 != 0:
            continue
        if n >= 8 and int(p[6] + p[7] + p[8]) % 13 != 0:
            continue
        if n >= 7 and int(p[5] + p[6] + p[7]) % 11 != 0:
            continue
        if n >= 6 and int(p[4] + p[5] + p[6]) % 7 != 0:
            continue
        if n >= 4 and int(p[2] + p[3] + p[4]) % 3 != 0:
            continue
        res += int(''.join(p))
    print(f'{n}: {res:11d}')

# 3:       22212
# 4:      711104
# 5:    12444480
# 6:   189838560
# 7:  1099210170
# 8:  1113342912
# 9: 16695334890
