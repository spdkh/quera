n = int(input())

while( n >= 10):
    x = 0
    while( n > 0):
        x += n % 10
        n = n // 10
    
    n = x
    
    
print(n)
