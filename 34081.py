n, k = map(int,input().split())

a = k % n
c = 1
while a != 0:
    a += k
    a = a%n
    c += 1
print(c)
