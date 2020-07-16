n, k = map(int,input().split())
a = [[] for i in range(n-1)]
a[0:n] = map(int, input().split())
x = 0
y = 0
for i in range(n):
    x += 1
    for j in range(k - 1):
##        print('a[i]:',a[i],'i,j:',i, j )

        if j == 0:
            y = a[i] 
        if y >= k:
            break

        a[i] = k
##        print('a:',a,'y:', y)
##        print(k - y - j) 
        if k - y - j in a:
            a[i] = k - j        
##            print('is in')
            x -= 1
            a[a.index(k - y - j)] = k   
            
            break   

print(n - x)    


