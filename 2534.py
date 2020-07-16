n = int(input())
h = [int(input()) for i in range(n)]

mean = sum(h)//n
s = 0
for i in range(n):
    if h[i] - mean > 0:
        s += h[i] - mean

print(s)


