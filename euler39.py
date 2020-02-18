#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 18:29:05 2020

@author: ms
"""

from tqdm import tqdm
Ns = [12, 80, 5*10**3+1]
# res = [0] * (max(Ns)+1)

import math
last = [0, 0]
res2 = [0]
# d = dict()
for n in tqdm(range(1, max(Ns) + 1)):
    # res[n] = res[n - 1]
    sol = 0
    for a in range(1, n // 3):
        b = 0.5 * n * (n - 2 * a) / (n - a)
        if b % 1 != 0:
            continue
        c = n - a - b
        if a >= b or b >= c or n != a + b + c:
            continue
        sol += 1
        # if n in d:
        #     d[n].append((a,b,c))
        # else:
        #     d.update({n: [(a,b,c)]})
    if sol > last[1]:
        last = n, sol
        # res[n] = n
        # with open('euler39_solution.txt', 'a') as f:
        #     f.write('\n'+str(n))
        res2.append(n)

# res2.append(math.inf)
for n in Ns:
    for i, x in enumerate(res2):
        if x <= n:
            continue
        print(res2[i - 1])
        break
with open('euler39_solution.txt', 'w') as f:
    f.write('\n'.join(map(str, res2)))
