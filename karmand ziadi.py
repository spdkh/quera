n = int(input())
s = []
colors = [0] * n
for i in range(n):
    x,y = map(str,input().split())
    s.append(x)
##    print(s)
    colors[i] = s.count(x)
##    print(colors)
    
print(max(colors))
