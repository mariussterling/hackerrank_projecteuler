#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 11:04:01 2020

@author: ms
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

N, M = map(int, input().split())

cube = list(combinations('0123456786', 6))

squares = [format(i ** 2, '0%id' % M).replace('9', '6')
           for i in range(1, N + 1)]


def valid1(c1):
    return all(x in c1 for x in squares)


def valid2(c1, c2):
    return all(x in c1 and y in c2
               or x in c2 and y in c1
               for x, y in squares)


def valid3(c1, c2, c3):
    return all(x in c1 and y in c2 and z in c3
               or x in c1 and y in c3 and z in c2
               or x in c2 and y in c1 and z in c3
               or x in c2 and y in c3 and z in c1
               or x in c3 and y in c1 and z in c2
               or x in c3 and y in c2 and z in c1
               for x, y, z in squares)


if M == 1:
    res = sum(1 for c1 in cube if valid1(c1))
elif M == 2:
    res = sum(
        1
        for i, c1 in enumerate(cube)
        for c2 in cube[:i + 1]
        if valid2(c1, c2))
elif M == 3:
    res = sum(
        1
        for i, c1 in enumerate(cube)
        # for j, c2 in enumerate(cube)
        for j, c2 in enumerate(cube[:i + 1])
        # for c3 in cube
        for c3 in cube[:j + 1]
        if valid3(c1, c2, c3))
print(res)
