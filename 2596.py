import time
begin = time.time()
import math

q = int(input())
a = list(map(int, input().split()))

def lcm(a, b):
    return a * b // math.gcd(a, b)

x = 1
for num in a:
    x = lcm(x, num)

c = 0
y = 1
s = set()
if x <= 1000:
##    print(x, y)
    s.update([x])
    i = 1
    for j in range(2, 1000 // x + 1):
        if len(s) > 1000 // x:
            break
        i += 1
        for j in range(2, 1000 // x + 1):
            m = y * j
            if m * x <= 1000:
##                print(m * x, y)
                s.update([m * x])
            else:
                break
        y *= i
            
print(len(s))
end = time.time()
print(end - begin)
