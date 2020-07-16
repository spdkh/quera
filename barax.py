n = 1
s = []
while(n != 0):
    n = int(input())
    s.append(n)

for i in range(len(s)-2,-1,-1):
    print(s[i])
