n, m = map(int,input().split())
a = [list(map(int,input().split())) for i in range(n)]
x = [0 for i in range(m)]
y = [0 for i in range(m)]
s = 0
for i in range(m):
    x[i], y[i] = map(int, input().split())
    s += a[x[i]-1][y[i]-1]

print(s)
