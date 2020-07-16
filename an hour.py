a,b = map(int,input().split())

h = (12 - a)%12
m = (60 - b)%60


if h < 10:
    print('0',end ='')

print(h,end=':')

if m < 10:
    print('0',end ='')

print(m)
