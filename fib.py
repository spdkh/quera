def fib(n):
    if n == 1 or n == 2:
        return n 
    return fib(n-1) + fib(n-2)

n = int(input())
s = []
x = 0
i = 0
while x <= 100:
    i += 1
    x = fib(i)
    s.append(x)
    
for i in range(1,n+ 1):
    if i in s:
        print('+',end='')
    else:
        print('-',end='')
    
