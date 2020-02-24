# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter


def is_pandigital(i):
    s = ''
    j = 1
    while len(s) < k:
        s += str(i * j)
        j += 1
    if len(s) != k:
        return False
    for i, v in Counter(s).items():
        if v != 1 or i < '1' or i > str(k):
            return False
    return True


n, k = list(map(int, input().rstrip().split()))
for i in range(2, n):
    if is_pandigital(i):
        print(i)
