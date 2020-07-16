a = [[]for i in range(3)]
a[0:3] = map(int, input().split())
i = 0
while(0 not in a):
    
    a[i%2*2] -= 1
    i += 1

if i % 4 == 0:
    print(i // 4,i // 4,i // 4,i // 4)
if i % 4 == 1:
    print(i // 4 + 1,i // 4,i // 4,i // 4,)    

if i % 4 == 2:
    print(i // 4 + 1,i // 4 + 1, i // 4,i // 4)
if i % 4 == 3:
    print(i // 4 + 1, i // 4 + 1,i // 4 + 1,i // 4)    
