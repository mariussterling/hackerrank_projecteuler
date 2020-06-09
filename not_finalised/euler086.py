# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt, ceil
t = int(input())
ms = [int(input()) for _ in range(t)]


def has_property(m):
    ret = 0
    for d in range(ceil(m/sqrt(2)), ceil(sqrt(2) * m)):
        tmp = sqrt(2 * d ** 2 - m ** 2)
        if tmp % 2 != 0:
            continue
        a = (m - tmp) / 2
        b = (m + tmp) / 2
        if a % 1 == 0 and a >= 1:
            ret += m
        if b % 1 == 0 and b >= 1:
            ret += m
    return ret
has_property(100)

res = [0 for i in range(max(ms) + 1)]
for i in range(3, max(ms)):
    res[i] += res[-1] + has_property(i)
for i in ms:
    print(res[i])
