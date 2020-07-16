a, b = map(int, input().split())

l = a % b
sum1 = l
sum2 = 0
c = 0
while a > 1:
    c += 1
    l *= 10
    a //= b
    l += a % b
    if c % 2 == 0:
        sum1 += a % b
    else:
        sum2 += a % b

print('Yes') if sum1 == sum2 else print('No')
