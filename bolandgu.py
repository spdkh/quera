a = input()
print(a)
a = list(a)

for i in range(len(a)):
    if i != len(a) - 1:
        for j in range(i + 1):
            a[j] = a[i+1]

        b = ''.join(a)
        print(b)
