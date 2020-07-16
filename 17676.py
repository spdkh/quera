
n, m = map(int, input().split())

ch = [(input()) for i in range(n)]

##c = 0
##
##for i in range(n):
##    for j in range(m , 0, -1):
##        c += ch[i].count(j * '|')
##        ch[i] = ch[i].replace(j * '|', j * '+')
####        print(ch[i], j * '|', i)
####        print(c)
##        
##ch = [''.join([row[i] for row in ch]) for i in range(len(ch[0]))]
##
##for i in range(m):
##    for j in range(n , 0, -1):
##        c += ch[i].count(j * '-')
##        ch[i] = ch[i].replace(j * '-', j * '+')
####        print(ch[i], j * '-', i)
####        print(c)
##print(c)
####end = time.time()
####print(end - start)
