import time
begin = time.time()

q = int(input())
a = list(map(int, input().split()))

c2 = 0
for i in range(a[0], 1001):
    c1 = 0
    for num in a:
        if i % num == 0:
            c1 += 1
##            print(i, num)
    if c1 == q:
        c2 += 1

print(c2)
end = time.time()
print(end - begin)
