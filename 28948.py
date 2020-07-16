import time
begin = time.time()
s = '=' * 50000 + 'a' * 30000 + '='* 10000#list(input())
s = list(s)
while '=' in s:
    if s[0] == '=':
        del s[0]
    else:
        idx = s.index('=')
        del s[idx - 1]
        del s[idx - 1]

print(''.join(s))
end = time.time()
print(end - begin)
