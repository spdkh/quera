a = int(input())
b = int(input())

def rev(a):
    c = 0
    d = a
    for i in range(3):
        c += (d % 10)
        c *= 10
        d = d // 10
    return c//10

if rev(a) < rev(b):
    print(a, '<', b)
elif rev(a) > rev(b):
    print(b, '<', a)
else:
    print(a, '=', b)
