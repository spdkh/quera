a, b, c = map(int, input().split())

x = []
y = []
for i in range(a):
    x.append(list(map(int, input().split())))

for i in range(b):
    y.append(list(map(int, input().split())))

for i in range(a):
    for k in range(c):
        s = 0
        for j in range(b):
            s += x[i][j]*y[j][k]
        print(s, end = ' ')
    print()


