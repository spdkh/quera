n = int(input())
names = []
x = [0 for i in range(n)]
for i in range(n):
    names.append(input())

    names[i] = list(names[i])
##print(names)
for k in range(n):
    for i in range(len(names[k])):
        if names[k][i] != '':    
            x[k] += 1
                
            for j in range(i,len(names[k])):
                if names[k][j] == names[k][i] and i != j:
##                        print(names[k][j])
                        names[k][j] = ''
        
##        print('i,j,x :', i,j,x, names)
##    names = ''.join(names)
##    y = len(names)
##    print(y)
##print(names)
print(max(x))
