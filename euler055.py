from collections import Counter

N = 130

def palindrom(x):
    return int(str(x)[::-1])
def is_palindrom(x):
    x == palindrom(x)
def find_palindrom(x, N):
    i = 0
    while i < 60 and not is_palindrom(x) and x <=N:
        i += 1
        x += palindrom(x)
    if x <= N:
        return x
    else:
        return N+1

c = Counter([find_palindrom(i, N) for i in range(1, N)])
c

x = 19
x += palindrom(x)
x
is_palindrom(x)