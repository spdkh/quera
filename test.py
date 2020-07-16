import time
s = ['a'] * 100000
##begin = time.time()
##while 'a' in s:
##    s[s.index('a')] = ''
##end = time.time()
##print("''", end - begin)
begin = time.time()
while 'a' in s:
    del s[0]
end = time.time()

print("del", end - begin)

s = ''.join(s)
begin = time.time()
a = []
while 'a' in s:
    a.append(a.index('a', 0, -1))
    s.replace('a', '')
end = time.time()
print(a)
print("replace",end - begin)
