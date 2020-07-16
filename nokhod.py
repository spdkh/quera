a,b,c = map(int, input().split())
tin = ['' for i in range(3)]
tout = ['' for i in range(3)]
for i in range(3):
    tin[i],tout[i] = map(int, input().split())
    
duration = max(tout) - min(tin)
scale = 80 //duration

for i in range(3):
    print(tin[i],tout[i])
    print((tin[i])* scale * ' ','|',(tout[i] - tin[i])* scale * '*','|')
    
if min(tout) > max(tin):
    commonc =  min(tout) - max(tin)
else:
    commonc = 0



for i in range(3):
    
    tout[i] -= commonc
    print(tin[i],tout[i])
    print((tin[i])* scale * ' ','|',(tout[i] - tin[i])* scale * '*','|')
    
commonb = 0
uncommon = 0
for i in range(3):
    for j in range(i+1,3):
        print('i,j: ',i,j)
        if (tin[i] <= tin[j] and tout[i] > tin[j]) or (tout[i] >= tin[j] and tin[i] < tout[j]):
            cb = min(tout[j],tout[i]) - max(tin[i],tin[j])
            print('cb:',cb)
            commonb += cb
            if tout[i] >= tin[i] + cb:


                tout[i] -= cb
            else:
                tout[i] = tin[i]
            if tout[j] >= tin[j] + cb:
                tout[j] -= cb
            else:
                tout[j] = tin[j]
    uncommon += tout[i]-tin[i]#duration - commonb - commonc
 
    print(tin[i],tout[i])
    print((tin[i])* scale * ' ','|',(tout[i] - tin[i])* scale * '*','|')
print('uncommon:',uncommon,'commonb', commonb,'commonc',commonc)


print(uncommon * a + commonb*2 * b + commonc* 3 * c)

