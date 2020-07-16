n = int (input())
a = list(map(int, input().split()))

def remover(a):
    while len(a) > 1:
        if a[1] >= a[0]:
            del a[0]
        else:
            break
    return a
mx = max(a)
##for i in range(n):
##    print(a[i] * '#'+ (mx - a[i]) * '0')
b = []
a = remover(a)
a = a[-1::-1]
a = remover(a)
high = a[0]
##print('a', a)

idx = len(a)
for i in range(1, len(a) - 1):     
    if high > a[i]:
        b.append(high - a[i])
    elif a[i] < mx:
        high = a[i]
    else:
        idx = len(a) - i
        break

##print('idx', idx)
##print('b:', b)
a = a[-1::-1]
high = a[0]
for i in range(idx):     
    if high > a[i]:
        b.append(high - a[i])
    else:
        high = a[i]

##print(b)
##    print(high, i)
print(sum(b))

