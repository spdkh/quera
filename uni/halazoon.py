n = int(input())

r = n % 4
a = n // 4

if r == 0:
    print( -1 * a, a)
elif r == 1:
    print( -1 * a, -1 * a)
elif r == 2:
    print( 1 + a, -1 * a)
else:
    print( 1 + a, 1 + a)
