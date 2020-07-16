n, k = map(int, input().split())

c = list(map(int, input().split()))
mn = max(c)
for i in range(1, n - 2):
    for j in range(i + 1, n - 1):
        a = min(max(c[:i]), max(c[i:j]), max(c[j:]))
        if mn > a:
            mn = a

print(mn)
