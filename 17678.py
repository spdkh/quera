n,d = map(int, input().split())

name = [set() for i in range(d)]
for i in range(n):
    s = input()
    name_ = s.split('|')[2].split(' ')[2]
    idx = int(s[7])-1
    name[idx].update([name_])

name_ = set()


for i in range(d):
    name_.update(name[i])
    number = len(name_) # total number of persons
    
    pn = len(name[i]) # number of persons in a day
    print(pn,end = ' ')

    intersect = set()
    for j in range(i - 1, -1, -1):
        intersect.update(name[i].intersection(name[j]))

    print(pn - len(intersect), end = ' ') if i != 0 else print(pn, end = ' ')
##    print()
##    print('first', intersect)
    
    intersect = set()
    for j in range(i + 1, d):
        intersect.update(name[i].intersection(name[j]))
##    print('last', intersect)
    
    print(pn - len(intersect), end = ' ') if i != d - 1 else print(pn, end = '')
    print()
    
