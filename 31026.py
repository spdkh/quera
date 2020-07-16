n = int(input())
a = input()
m = int(input())
o = input()

c = 0
A = list(a)
B = list(o)
while A != B:
    c += 1
    A.pop()
    B.pop()

i = 0
B = list(o)
while A != B:
    A.append(B[m - c + i])
    i += 1
    
print(c + i)
    
