from collections import Counter
fac = {0: 1, 1: 1,2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320,
       9: 362880}

def next(x):
    c = Counter(str(x))
    return sum([fac[int(k)] * v for k,v in c.items()])


def length_rep(n):
    global res
    if n in res:
        return
    l = [n]
    while l[-1] not in l[:-1] and l[-1] not in res:
        l.append(next(l[-1]))
    if l[-1] in l[:-1]:
        # save cyclic values
        ll = l.index(l[-1])
        ln = len(l)
        res.update({l[i]: ln - ll - 1 for i in range(ll, ln)})
        l = l[:ll + 1]
    # save non-cyclic values
    off = res[l[-1]]
    ln = len(l)
    res.update({x: off + ln - i - 1 for i, x in enumerate(l[:-1])})

NL = []
T = int(input())
for _ in range(T):
    NL.append(list(map(int, input().split())))
N = max([i[0] for i in NL])
res = dict()
for i in range(N + 1):
    length_rep(i)

for (N, L) in NL:
    tmp = [str(k) for k, v in res.items() if v == L and k <= N]
    if tmp:
        print(' '.join(tmp))
    else:
        print(-1)
    del tmp
