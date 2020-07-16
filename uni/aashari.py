n = int(input())

a = float(input())
mx = a
mn = a
s = a
for i in range(n - 1):
    a = float(input())
    mx = a if a > mx else mx
    mn = a if a < mn else mn
    s += a

av = s / n

print('Max:', "%.3f" % mx)
print('Min:', "%.3f" % mn)
print('Avg:', "%.3f" % av)
