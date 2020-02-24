# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import sqrt

n, a, b = map(int, input().rstrip().split())

def hexa(n):
    return n * (2 * n - 1)
def pent(n):
    return n * (3 * n - 1) // 2

def is_tri(x):
    return sqrt(1 + 8 * x) % 2 == 1
def is_pent(x):
    return sqrt(1 + 24 * x) % 6 == 5

if b == 6:
    f = hexa
elif b == 5:
    f = pent
if a == 5:
    iss = is_pent
elif a == 3:
    iss = is_tri

for i in range(1, n):
    p = f(i)
    if p >= n: break
    if iss(p):
        print(p)
    

