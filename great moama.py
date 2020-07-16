n,s = input().split()
n = int(n)
l = [0 for i in range(n)]
r = l[:]
s = list(s)
for i in range(n):
    l,r = map(int,input().split())
    l-= 1
    r-=1
    print(s[:l])
    s2 = s[l:r+1]
    s2.reverse()
    print(s[l:r+1],s2)
    print(s[r+1:])
   # if int(''.join(s2)) > int(''.join(s[l:r+1])):
    s = s[:l]+s2+s[r+1:]
    

    print(''.join(s))
    
