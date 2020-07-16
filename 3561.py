n = int(input())

print(4 * n * ' ' + '*')

for row in range(1,n+1):
    for line in range(3):
        print(4 * (n - row) * ' ', end = '')
        for j in range(row):
            print((3 - line) * ' ' + '*', end = '')
            print((line * 2 + 1) * ' ' + '*', end = '')
            if j != row - 1:
                print((3 - line - 1) * ' ', end = '')

        print()
    print((4 * (n - row) * ' ')+(8 * row + 1) * '*' )
