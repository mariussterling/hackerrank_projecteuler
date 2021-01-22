#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 10:36:14 2020

@author: ms
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
from operator import itemgetter
k, l, b = list(map(int,input().strip().split()))
# k,l,b = 1,1,1

squares = []
squares_lb = []
# x0, y0, x, area=x**2, l, b
s0 = {'x0': 1, 'y0': 0, 'x': None, 'area': None, 'l': 0, 'b': 0}
stop_crit = {'area': math.inf, 'rank': 0}
def compute_x(s):
    s = dict(s)
    res = s['x0'] - s['y0']
    s['x'] = 0.5 * ( res + math.sqrt(res**2 + 4))
    s['area'] = (s['x'] - s['x0']) ** 2
    return s
def square_right(s):
    s = dict(s)
    s['x0'] = s['x']
    s['x'] = None
    s['area'] = None
    s['l'] += 1
    s = compute_x(s)
    return s

def square_up(s):
    s = dict(s)
    s['y0'] += s['x'] - s['x0']
    s['x'] = None
    s['area'] = None
    s['b'] += 1
    s = compute_x(s)
    return s

def next(s0, l, b, k):
    global squares
    global squares_lb
    s1 = square_right(s0)
    if s1['l'] == l and s1['b'] == b:
        squares_lb.append(s1)
    else:
        squares.append(s1)
    s2 = square_up(s0)
    if s2['l'] == l and s2['b'] == b:
        squares_lb.append(s2)
    else:
        squares.append(s2)
    # squares.append(s2)
    stop = sorted(squares_lb, key=itemgetter('area'))
    if len(stop) < k:
        next(s1, l, b, k)
        next(s2, l, b, k)
    else:
        stop_area = stop[k - 1]['area']
        if s1['area'] >= stop_area:
            next(s1, l, b, k)
        if s2['area'] >= stop_area:
            next(s2, l, b, k)
    
    

if l == 0 and b == 0:
    print(1)
else:
    s1 = compute_x(s0)
    squares.append(s1)
    next(s1, l, b, k)
    squares.extend(squares_lb)
    d = {r+1:s for r, s in enumerate(sorted(squares, key=itemgetter('area'), reverse=True))}
    print(sorted([r for r, s in d.items() if s['l'] == l and s['b'] == b])[k])


