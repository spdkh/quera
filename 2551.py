a = input()
sign = input()
b = input()

if sign == '+':
    print(int(a) + int(b))
else:
    print('1' + '0' * (len(a) + len(b) - 2))
