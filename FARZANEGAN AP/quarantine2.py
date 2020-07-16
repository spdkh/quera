n = int(input())

e = n
f = 1
while e >= 0:
    print(e * ' ' + '*' * f)
    e -= 1
    f += 2

e += 1
f -= 2

while e <= n:
    e += 1
    f -= 2
    print(e * ' ' + '*' * f)
    
