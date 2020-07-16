n = int(input())

m = n
r = 0

while(m > 0):   
    r *= 10
    r += (m % 10)
    m //= 10

if n == r:
    print('YES')
else:
    print('NO')        
