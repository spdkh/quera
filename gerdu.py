n, x, y = map(int, input().split())
a = -1
b = n // min(x,y) + 1
for i in range(b):
    for j in range(b):
        if i * x + j * y == n:
            a = i
 
            print(i, j)
            break
    if a != -1:
        break
    
if i == b - 1 and j == b - 1:
    print(-1)

