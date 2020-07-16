x = [ '' for i in range(3)]
y = x[:]

for i in range(3):
    x[i], y[i] = map(int,input().split())

if x[0] != x[1]:
    if x[0] != x[2]:
        xs = x[0]
    else:
        xs = x[1]
else:
     xs = x[2]

if y[0] != y[1]:
    if y[0] != y[2]:
        ys = y[0]
    else:
        ys = y[1]
else:
     ys = y[2]

print(xs, ys)
