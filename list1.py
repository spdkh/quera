a, b, c, d, e, f = map(int, input().split())
s = [d, e, f]
s.sort()
if a > b:
    maxim = a
    minim = b
else:
    maxim = b
    minim = a
    
if maxim >= s[1] and minim >= s[0]:
    print('zende mimuni')
else:
    print('dari mimiri')



