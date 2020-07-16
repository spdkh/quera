L,R = map(int,input().split())
s1=['1']
s2=s1
while len(s2) <= R:
    s1 = ['0' if s1[j] == '1' else '1' for j in range(len(s1))]
    #print(s1)
    s2.extend(s1)
    #print(s2)
    s1 = s2
print(''.join(s2[L-1:R]))
