def conv_to10(a, b):
    o = 0
    i = 0
    while a > 0:
        o += (a % 10)*b ** i
        i += 1
        a //= 10
    return o

def conv_toc(a, b):
    o = 0
    i = 0
    while a > 0:
        o += (a % b)*10 ** i
        i += 1
        a //= b
    return o

a = int(input())
b = int(input())
c = int(input())

a = conv_to10(a, b)
a = conv_toc(a, c)

print('YES') if a == int(str(a)[-1::-1]) else print('NO')


