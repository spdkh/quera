a = int(input())
b = int(input())

l = a - b
if l <= 0:
    print('Wrong order!')
elif l % 2 == 1:
    print('Wrong difference!')
else:
    for i in range(l // 2):
        print(a * '* ')
        
    for i in range(b):
        print(l // 2 * '* ' + b * '  ' + l // 2 * '* ')
        
    for i in range(l // 2):
        print(a * '* ')
