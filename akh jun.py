n = []
s = [[] for i in range(3)]
s2 = []
hafte = [str(i)+'shanbe' for i in range(7)]
hafte[0] = 'shanbe'
hafte[6] = 'jome'
for i in range(3):
    n.append(int(input()))
    s[i] = [[] for j  in range(n[i]-1)]
    s[i][0:n[i]-1] = map(str, input().split())
    s2 = sum(s, [])

x = 0
for i in range(7):
    if hafte[i] not in s2:
        x += 1
print(x)
