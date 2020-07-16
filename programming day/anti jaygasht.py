n = 3
counter = 2 * n - 1
a = [1, 2, 2, 3, 3, 4, 5, 5, 4, 1]
s = []
p = []
while a[counter] != a[counter - 1]:
    s.append(a[counter])
    a.pop()
    counter -= 1
    print('while2         ', counter, a, s, p)

if a[counter] == a[counter - 1]:
    p.append(a[counter])
for i in range(n - 1, -1, -1):
    if counter <= 0:
                break
    while len(s) > 0:
        a.pop()
        s.pop()
        counter -= 1
        print('for          ', i, counter, a, s, p)
        if counter <= 0:
                break
    if counter > 0:
        print('yes')
        while a[counter] != a[counter - 1]:
            s.append(a[counter])
            a.pop()
            counter -= 1
            if counter <= 0:
                break
            if a[counter] == a[counter - 1]:
                p.append(a[counter])
            print('while1       ', i, counter, a, s, p)


print(p)
