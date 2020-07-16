
a = []
s = 0
p = 1
for i in range(4):
    a.append(int(input()))
    s += a[i]
    p *= a[i]

print('Sum : %.6f' % s)
print('Average : %.6f' % (s/4))
print('Product : %.6f' % p)
print('MAX : %.6f'% max(a))
print('MIN : %.6f'% min(a))
