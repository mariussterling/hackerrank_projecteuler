#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 20:39:40 2020

@author: ms
"""

palindromelist = sorted(set([i * j for i in range(100, 1000) for j in range(100, 1000) if
     str(i * j) == str(i * j)[::-1] and i * j >= 101101
     ]), reverse=True)

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        a = int(input())
        for i in palindromelist:
            if i < a:
                print(i)
                break