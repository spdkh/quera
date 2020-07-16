cnt = 1
def fcn(b, w):
    global cnt

##    print(b, w)
    
    if b <= 0 and w <= 0:
##        print('', cnt, '- 1 1:', 0, 0)
        cnt += 1
        return 0, 0
    
    if (b == 1) or (b % 2 == 1 and w == 0):
##        print('2number', cnt, '- 1 1:', 1, 0)
        cnt += 1
        return 1, 0
    
    if (b <= 0) or (b == 0 and w == 2) or (b % 2 == 0 and w == 0):
##        print('3number', cnt,'-', b, w, ':', 0, 1)
        cnt += 1
        return 0, 1

##    print('_____recursion_____')
    b1, w1 = fcn(b - 2, w + 1)
    b2, w2 = fcn(b, w - 1)

    if (b1 == b2) and (w1 == w2):
##        print('recurse ', cnt,'-', b, w, ':', b1, w1)
        cnt += 1
        return b1, w1
    
##    print('?', cnt,'-', b, w, ':', 0, 0)
    cnt += 1
    return 0, 0

##b, w = map(int, input().split())
for b in range(30):
    for w in range(30):
##        print(fcn(b, w), end = '|')
        if fcn(b, w) == (0, 1):
            print('w', end = '|')
        elif fcn(b, w) == (1, 0):
            print('b', end = '|')
        else:
            print('?', end = '|')
    print()
##if fcn(b, w) == (0, 1):
##    print('white')
##elif fcn(b, w) == (1, 0):
##    print('black')
##else:
##    print('noprediction')
