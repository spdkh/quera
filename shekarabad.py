n, m = map(int,input().split())
s = []
x = 0
for i in range(n):
    s.append(input())
    x += s[i].count('*')
s = list(s)

print(x)
