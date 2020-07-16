def check(a, hashtag):

    la = len(str(a))
    lh = len(hashtag)
    if lh > 1:
    ##    print(la, lh)
        idx = hashtag.index('#')
        idx = lh - hashtag.index('#')
        hashtag = int(hashtag.replace('#', ''))
        
    ##    print(idx)
        checked = (a % (10 ** (idx - 1))) +\
        (10 ** (idx - 1))*(a//(10 ** (la - lh + idx))) 
    ##    print(a, checked, hashtag)
        if hashtag != checked or la < lh:
            return -1
    return 1

s = input().replace(' + ', ' ')
s = s.replace(' = ', ' ')
s = s.split(' ')

for i in range(2):
    if '#' in s[i]:
        hashtag = s[i]
        s[i] = int(s[2]) - int(s[1 - i])
        flag = check(s[i], hashtag)
##        print('flga',  flag, s[i], hashtag)
        break
##print(flag)       
if '#' in s[2]:
    hashtag = s[2]
    s[2] = int(s[1]) + int(s[0])
    flag = check(s[2], hashtag)

if flag == -1:
    print(-1)
else:
    print(s[0],'+', s[1], '=', s[2])


