import time

def is_prime(n):
    if n == 1:
        return 0
    if n % 2 == 1:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                n = 0
                break
        return n
    return 0

def is_strong(n):
    
    if is_prime(n):
        
        x = (n // 10)
        if x == 0:
            return n
##        if (n) % 2 != 0:
        return is_strong(x)
    return 0

n = int(input())
begin = time.time()
if n == 1:
    print(2)
    a = 1
else:
    a = int('2' + '3'*(n - 1))

for i in range(a , 10 ** n, 2):
    b = str(i)
    if ('5' not in b[1:]):
        if is_strong(i):
            print(i)

print(time.time() - begin)
