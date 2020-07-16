n, x, k = map(int, input().split())
s = [input() for i in range(n)]

i = x
for j in range(k):
    if i < n:
        i += 1
    else:
        i = 1

print(s[i - 1])
