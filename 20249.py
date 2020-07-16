import math
n, k = map(int,input().split())
a = list(map(int, input().split()))

s = sum(a)
print(n - math.ceil(s / k))
    
