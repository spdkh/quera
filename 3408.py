n = int(input())
b = input()
j = len(b)
a = ''

for i in range(len(b)-1,0,-1):
    if b[i] == ' ':
        a += b[i+1:j] + ' '
        j = i
for i in range(len(b)):
    if b[i] == ' ':
        a += b[0:i]
        break
print(a)
