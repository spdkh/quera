import math
a, b , x = map(int, input().split())

def m(a):
    l = [1]
    for i in range(2, a + 1):
        if a % i == 0:
            l.append(i)
    return l

c = 0
if a + b <= x:
    c = len(m(a)) * len(m(b))
else:
    for i in m(a):
        for j in m(b):
            if i + j <= x:
                c += 1

print(c)
