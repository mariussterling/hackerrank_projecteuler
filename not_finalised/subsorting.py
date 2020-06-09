#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:16:18 2020

@author: ms
"""
import tqdm
if False:
    n, q, k = [int(i) for i in '10 10 0'.split()]
    a = [int(i) for i in '-270846877 217106325 -591735326 880116462 -106469914 -630766902 -404429578 255940605 446894699 69407501'.split()]
    queries = """4 9
    2 6
    0 5
    5 9
    2 5
    2 6
    1 5
    1 8
    3 8
    0 0"""
    queries = [[int(x) for x in q.split()] for q in queries.split('\n')]
f = open("input10.txt", "r")
n, q, k = [int(i) for i in f.readline().split()]
a = [int(i) for i in f.readline().split()]
queries = []
for _ in tqdm.tqdm(range(q)):
    queries.append(list(map(int, f.readline().rstrip().split())))


def sortedSubsegments(k, a, queries):
    a2 = list(a)
    for i in range(len(queries) - 1, 0, -1):
        if k < queries[i][0] and k > queries[i][1]:
            queries.pop()
        else:
            break
    ids = set()
    for q in tqdm.tqdm(queries):
        a2[list(set(range(q[0], q[1] + 1)).intersection(ids))]
        set(range(q[0], q[1] + 1)).difference(ids)
        a2[q[0] : q[1]+1] = sorted(a2[q[0] : q[1]+1])
        ids.update(range(q[0],q[1]))
        if a2 == a3:
            return a3[k]
    return a2[k]

sortedSubsegments(k, a, queries)



def mergeArrays(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    arr3 = [None] * (n1 + n2) 
    i = 0
    j = 0
    k = 0
  
    # Traverse both array 
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]: 
            arr3[k] = arr1[i]
            i += 1
        else: 
            arr3[k] = arr2[j]
            j += 1
        k += 1
    while i < n1: 
        arr3[k] = arr1[i]; 
        k += 1
        i += 1
    while j < n2: 
        arr3[k] = arr2[j]; 
        k += 1
        j += 1
    return arr3

mergeArrays([1,3,5,7,8,9,10,11,12,13], [4,4,6])



from itertools import chain

print ("Concatinated two range() function")
concatenated_range = chain(range(5), range(4, 20))
print(list(concatenated_range))
10 in range(20)
r = range(20)
print([i for i in r.__dir__() if i[:2] != '__'])

