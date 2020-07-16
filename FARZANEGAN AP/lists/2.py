n = int(input())

a = [int(input()) for i in range(n)]

begin = -1 if n % 2 == 0 else -2
b = a[begin:0:-2]
print(b)
