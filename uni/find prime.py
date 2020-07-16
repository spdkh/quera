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

n = int(input())

a = n
s = 0
while a  > 0:
    s += a % 10
    a //= 10

i = n
cnt = 0
while cnt < s:
    i += 1
    if is_prime(i):
        cnt += 1
    

print(i)
