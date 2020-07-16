
n = 38000#int(input())

flag = 0
for i in range(3, n//4 + 1):
    for j in range(i + 1, n//2):
        r = (n - (i) - (j))
        
        if r ** 2 == i ** 2 + j ** 2:
            print(i, j, r)
            flag = 1
            break
    if flag == 1:
        break
if flag == 0:
    print('Impossible')
