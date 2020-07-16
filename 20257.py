k, a, b = map(int, input().split())
t11 = 0
t12 = 0

if a == b:
    print(0)
else:
    ##t2 = (b - a)// k - 1 if (b - a)% k == 0 else (b - a)// k
    if a % k >= k / 2:
        t11 += (k - a % k)% k
##        print('begin >= k / 2,', (k - a % k)% k)
        a += t11
    else:
        t11 += a % k
##        print('begin < k / 2,', a % k)
        a -= t11

    if b % k > k / 2:
        t12 += (k - b % k)% k
##        print('end >= k / 2,', (k - b % k)% k)
        b += t12
    else:
        t12 += b % k
##        print('end < k / 2,', b % k)
        b -= t12

##print(a, b)
t2 = (abs(b - a))// k
print(t11 + t12 + t2)
