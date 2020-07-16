n = int(input())
sgozashte = input()
sneveshte = input()
x = 0
for i in range(n):
    if sgozashte[i] == sneveshte[i]:
        x += 1

print(n - x)
