n = int(input())
s = input()
s = list(map(int,list(s)))
        
k = []
for i in range(n // 6 + 1):
    k.extend([3, 3, 1, 1, 2, 2])

nz = []
for i in range(n // 3 + 1):
    nz.extend([1, 2, 3])

sf = []
for i in range(n // 4 + 1):
    sf.extend([2, 1, 2, 3] )

l1 = [k,nz,sf]
l2 = []
mark = []
for i in range(3):
    l2.append([l1[i][j] - s[j] for j in range(n)])
    mark.append(l2[i].count(0))

d = ['keyvoon', 'nezam', 'shir farhad']
maxi = max(mark)
print(maxi)
while maxi in mark:
    print(d[mark.index(maxi)])
    mark[mark.index(maxi)] = -1

