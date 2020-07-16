s = input()
y = []
for i in range(len(s)):
    order = int(ord(s[i]))
##    print(i, s[i], order)
    if order <= 90:
        y.append(chr(((s.count(s[i]) * (order - 65) + 1)% 26) + 65))
    else:
        y.append(chr(((s.count(s[i]) * (order - 97) + 1)% 26) + 97))

print(''.join(y))
