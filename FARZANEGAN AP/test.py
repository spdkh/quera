import time

def is_prime(n):
    if n == 1:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            n = 0
            break
    return n

def is_strong(n):
    if is_prime(n):
        if n//10 == 0:
            return n
        if n % 2 != 0:
            return is_strong(n // 10)
    return 0

n = int(input())
begin = time.time()
print(is_strong(n))
print('recursion: ',time.time() - begin)

begin = time.time()
flag = 1
while n//10 > 0:
    if is_prime(n):
        n //= 10
    else:
        flag = 0
        break

print(flag)
print('for: ',time.time() - begin)

