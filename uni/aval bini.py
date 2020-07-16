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

a = int(input())
b = int(input())

x = []
for i in range(a + 1, b):
    if is_prime(i):
        x.append(i)

for i in range(len(x) - 1):
    print(x[i], end = ',')

if (len(x) > 0):
    print(x[len(x) - 1])
