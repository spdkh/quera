n, t2= map(str,input().split())
t = list(t2)
for i in range(len(t)):
    if t[i] in t[i+1:]:
        t[i] = ''
t = ''.join(t)

s2 = []
s = []
for i in range(int(n)):
    s2.append(input())
    s.append( list(s2[i]))

for i in range(int(n)):
    x = 0
    y = 0
    
    for j in range(len(t)):
        if t[j] in s[i]:
            y += 1
            for k in range(len(s[i])):
                if  s[i][k] == t[j]:
                    s[i][k] =''


    x = s[i].count('')
                

    if x == len(s[i]) and y == len(t):
        print('Yes')
    else:
        print('No')
