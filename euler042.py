from math import sqrt

t = int(input())

def check(x):
    x = sqrt(1 + 8 * x)
    if x % 2 != 1:
        return -1
    return int((x - 1) // 2)

for _ in range(t):
    print(check(int(input())))

