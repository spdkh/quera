n, k = map(int, input().split())
a = list(map(int, input().split()))

b = []
i = 0
while i < n:
    
    b.append(a[i])
    j = i + 1
    
    while  j < n:
        
        if b[i]+a[j] <= k:
            b[i] += a[j]
            del a[j]
            n -= 1
            j -= 1
        else:
            break
        
        j += 1
    i += 1
    
print(len(b))
