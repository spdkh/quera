n = int(input())

a = [int(input()) for i in range(n)]

s = 0
for i in range(n):
    s += a[i]

print(s)
