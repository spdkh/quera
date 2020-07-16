n = int(input())


a = [input() for i in range(n)]
b = [[] for i in range(n)]
mx = str(max(list(map(int, a))))
l = (8 - len(mx)%8) + len(mx)
##print(mx, l)
for i in range(n):
    a[i] = '0'*(l - len(a[i])) + a[i]
    for j in range(len(a[i]) // 8):
        b[i].append(a[i][j * 8:j * 8 + 8])
        
##print(b)
s2 = ''
c = 0
for i in range(-1, -l // 8 - 1, -1):
    s = c
    for j in range(n):
        s += int(b[j][i])
##    print(s)
    s = str(s)
    l2 = len(s)
    if l2 >= 9:
        c = int(s[:l2 - 8])
##        print('#', c)
        s = s[l2 - 8:]
##    print(s)
    s2 = s + s2
print(s2)
    
    
