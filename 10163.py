a,b,c = map(int, input().split())
tin = ['' for i in range(3)]
tout = ['' for i in range(3)]

for i in range(3):
    tin[i],tout[i] = map(int, input().split())
    
if min(tout) > max(tin):
    commonc =  min(tout) - max(tin)
else:
    commonc = 0

for i in range(3):   
    tout[i] -= commonc

commonb = 0
uncommon = 0
t = tout[:]
for i in range(2):
    for j in range(i+1,3):

        if (tin[i] <= tin[j] and tout[i] >= tin[j]) or (tin[i] > tin[j] and tin[i] < tout[j]):
            cb = min(tout[j],tout[i]) - max(tin[i],tin[j])

            commonb += cb
            t[i] -= cb
            t[j] -= cb
    uncommon += t[i] - tin[i]
uncommon += t[2] - tin[2] 
##print('uncommon:',uncommon,'commonb', commonb,'commonc',commonc)


print(uncommon * a + commonb*2 * b + commonc* 3 * c)
