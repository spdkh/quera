n,p,q = map(int, input().split())
n2 = n
s = [input() for i in range(n)]
c = 0
#print(s)
for i in range(n):
    j = i+1
    while j < n :
        print(s[i],s[j],s[i][:p] ,s[j][:p] , s[i][-1:-q-1:-1], s[j][-1:-q-1:-1], c)
        if s[i][:p] == s[j][:p] and s[i][-1:-q-1:-1] == s[j][-1:-q-1:-1]:
            del s[j]
            n-= 1
            j -= 1
            c += 1
        j+=1

print(n2 - c)
