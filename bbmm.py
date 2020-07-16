def bmm(a,b):
    x = min(a,b)
    y = max(a,b)
    out = 1
    while out != 0:
        out = y % x
        y = x
        x = out
    return y

n = int(input())
x = [0 for i in range(n)]
x[:] = map(int,input().split()) 
s = []
for i in range(n-1):
    for j in range(i + 1, n):
        a = bmm(x[i],x[j])
        s.append(a)

print(max(s))
