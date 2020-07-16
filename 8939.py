s = input().split(' + ')
s[1] = s[1].split(' = ')

if '#' not in s[0]:
    b = int(s[0])
    a = s[1][0]
    n = 2
else:
    b = int(s[1][0])
    a = s[0]
    n = 1

idx = len(a) - a.index('#')
l = len(a)
print(idx)
a = int(a.replace('#', ''))
c = int(s[1][1])
l2 = len(str((c - b)))
##if idx == 0:
##    real = 1((c - b)//(10 ** (l2 - l + idx)))
##else:
real = (10 ** (idx - 1))* ((c - b)//(10 ** (l2 - l + idx)))\
       + (c - b) % (10 ** (idx - 1))
answer = c - b
print(real , a)

if real == a:
    if n == 1:
        print(answer,'+', b, '=', c)
    else:
        print(b,'+', answer, '=', c)
else:
    print(-1)
