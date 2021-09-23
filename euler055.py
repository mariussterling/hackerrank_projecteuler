from collections import Counter

N = int(input())

def reverse(x):
    return int(str(x)[::-1])
def is_palindrom(x):
    return str(x) == str(x)[::-1]
def find_palindrom(x):
    i = 0
    while i < 60:
        if is_palindrom(x):
            return x
        i += 1
        x += reverse(x)
        
c = Counter([find_palindrom(i) for i in range(0, N + 1)])
if None in c:
    c.pop(None)
res = c.most_common(1)[0]
print(f"{res[0]} {res[1]}")