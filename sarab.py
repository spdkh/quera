t = int(input())
x = [[] for i in range(t)]
y = [[] for i in range(t)]
for i in range(t):
    x[i] , y[i] = map(int,input().split())

for i in range(t):
    if x[i] == y[i]:
        print(2 * x[i] - (x[i] % 2))
    elif x[i] - y[i] == 2:
        print(x[i] + y[i] - (y[i] % 2))
    else:
        print(-1)
