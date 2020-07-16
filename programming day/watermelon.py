n = int(input())
w = list(map(int, input().split()))
v = w[:]

i = 0
while len(w) >= 1 and i < n - 1:
    del w[w.index(min(w[i], w[i + 1]))]
    n -= 1

print(v.index(w[0]) + 1)

