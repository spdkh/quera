

n, k = map(int, input().split())

s = set(1)
a = [1] * n
i = n - 1
while i > 0:
    i -= 1
    del a[i + 1]
    a[i] = n - i
##    if a[i] > k:

    if a[i] > 2:
        for j in range(k):
        
    s.update(a[i])
