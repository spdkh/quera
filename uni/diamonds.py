n = int(input())

f = 1
while f <= n:
    print(((n - f)//2 * ' ' + '*' * f + (n - f)//2 * ' ')* 2)
    f += 2

f -= 2
while f >= 0:
    f -= 2
    print(((n - f)//2 * ' ' + '*' * f + (n - f)//2 * ' ')* 2)

