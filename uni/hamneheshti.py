a, b = map(int, input().split())

x = abs(a - b)
for i in range(2, x // 2 + 1,):
    if x % i == 0:
        print(i, end = ' ')

print(x)
