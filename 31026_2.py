n = int(input())
a = input()
m = int(input())
o = input()

i = 0
for j in range(min(m,n)-1):
##    print(j)
    if a[i] == o[i]:
    
        a = a[i+1:]
        o = o[i+1:]
##        print(a,o)
    else:
        break
print(len(a) + len(o))
