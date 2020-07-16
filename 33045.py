n = int(input())

def m(a):
    l = {1}
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            l.add(i)
    l.add(a)
    return list(l)

s = []
for i in range(1,n + 1):
##    print(m(i))
    s.extend(m(i))

print(len(s), sum(s))
