a = []
n = []
for i in range(5):
    a.append(input())
    if 'MOLANA' in a[i] or 'HAFEZ' in a[i]:
        n.append(i+1)
if (n != 0):
    for i in range(len(n)):
        print(n[i],end = ' ')
else:
    print('NOT FOUND!')
    
