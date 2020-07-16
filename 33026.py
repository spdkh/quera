n = int(input())
s1 = dict()
printed = []
for i in range(n):
    s = input()
    if ' := ' in s:
        key = s.split(' :=')[0]
        value = s.split(' :=')[1]
        s1.update({key:value})
    if 'print' in s:
        s = s.replace('[',' ')
        s = s.replace(']',' ')
        
        name = s.split(' ')[1]
        value = s.split(' ')[2]
        
        if '"' in s1[name]:
            printed.append(s1[name][s1[name].index(value) + 5])
        else:
            s1[name] = s1[name].replace(' ','')
            printed.append(s1[name][int(value)*2+1])

for i in range(len(printed) - 1):
    print(printed[i])
print(printed[len(printed) - 1], end = '')