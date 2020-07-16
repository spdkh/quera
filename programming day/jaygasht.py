def old_little_code(n, p):
##    p = list(range(i + 1))
    print('p', p)
    s = []
    a = len(p) * 2 * [0]
    print(a)
    counter = 0
    for i in range(n):
        while len(s) > 0 and p[s[0]] < p[i]:
            a[counter] = s[-1]
            counter += 1
            s.pop()
            print('while1     ',i, counter, a, s)
        s.append(i + 1)
        a[counter] = s[-1]
        counter += 1
        print('for        ',i, counter, a, s)

        
        
    while len(s) > 0:
        a[counter] = s[-1]
        counter += 1
        s.pop()
        print('while2       ', counter, a, s)

        
    return a
##def  anti_code(a):
    
##n = int(input())
##a = list(map(int, input().split()))

##for i in range(1, n):
##print(old_little_code(n,[2, 1]))
##b = a[n//2:]
##b.sort()
##b.reverse()
##if a[n//2:] == b:
##    print(1)
##else:
##    pass
print(old_little_code(4, [5, 1, 2, 4]))
