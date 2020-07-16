a = list(map(int, input().split()))

mean = sum(a)/3

s = 0
if mean != 0:
    for i in range(3):
        n = a[i] // mean
        if n != a[i] / mean: 
            s += n
        else:
            s += n - 1

print(int(s))
