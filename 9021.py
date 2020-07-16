n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
for i in range(n):
    if b[i] == 1: 
        c.append(a[i])

c.sort()
for i in range(len(c)):
    print(c[i], end = ' ')  

