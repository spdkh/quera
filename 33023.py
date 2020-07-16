n,m = map(int,input().split())

a = [list(map(int, input().split())) for i in range(n)]

c = 0
for i in range(1, n-1):
    for j in range(1, m-1):
        x1 = a[i][j] - a[i-1][j]
        x2 = a[i][j] - a[i+1][j]
        y1 = a[i][j] - a[i][j-1]
        y2 = a[i][j] - a[i][j+1]
        if x1 * x2 > 0 and y1 * y2 > 0 and x1 * y1 < 0:
            c += 1
            
print(c)
