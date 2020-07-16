n, m = list(map(int, input().split()))

if (n / m == n//m):
    print(n//m)
else:
    print(n//m + 1)
