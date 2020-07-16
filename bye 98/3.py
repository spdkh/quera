def moveL(x, y, cnt):
    if cnt % 2 == 0:
        x -= 1
    else
        x += 1
    y += 2
    return x, y

n , m = map(int, input().split())

a= [list(map(int, input().split())) for i in range(n)]

b = a[:][:]

x = a[-1].index(max(a[-1]))
print(x)
for i in range(n):
    for j in range(m):
        
