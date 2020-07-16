n = int(input())

a = [int(input()) for i in range(n)]
b = [int(input()) for i in range(n)]

c = list(map(lambda x,y: x ** 2 + y ** 2, a, b))

for i in range(n):
    print(c[i])
