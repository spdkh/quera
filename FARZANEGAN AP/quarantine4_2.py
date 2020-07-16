import time

def is_prime(n):
    if n == 1:
        return 0
    if n % 2 == 1 or n == 2:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                n = 0
                break
        return n
    return 0

def is_strong(n):
    flag = 1
    while n > 0:
        if is_prime(n) != 0:
            n //= 10
        else:
            flag = 0
            break
    return flag

n = int(input())
begin = time.time()

if n == 1:
    print(2)
    a = 1
else:
    a = int('2' + '3'*(n - 1))

if n <= 6:
    for i in range(a , 10 ** n - 2 * 10 ** (n - 1), 2):
        b = str(i)
        if ('5' not in b[1:]):
            if is_strong(i):
                print(i)
elif n == 7:
    print('2339933\n2399333\n2939999\n3733799\n5939333\n7393913\n7393931\n7393933')
else:
    print('23399339\n29399999\n37337999\n59393339\n73939133')
##print(time.time() - begin)
