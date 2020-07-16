k = int(input())
s = input()

s2 = [input() for i in range(k)]
c = 0
for i in range(k):
    a = s2[i].index(s[i])
##    print(a)
    if a >= 5:
        a = 9 - a
##    print(a)
    c += a

print(c)
