n = int(input())

cnt = 0

for i in range(n):
    a = int(input())
    if i == 0:
        last = a
    if a != last:
        cnt += 1
    last = a
    
    

print(cnt)
