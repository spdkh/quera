n, m = map(int, input().split())


b = 1
a = [b]
for i in range(1, n):
    b += n // 2 + 1 if n % 2 == 1 else n // 2 
    b = b % n
    if b % n == 0:
        b += n
##    print(a[i - 1], b, abs(b - a[i - 1]), m)
##    print(a, b)
    if b not in a and abs(b - a[i - 1]) >= m:
        a.append(b)
##        print(a)
    elif b in a:
        b = (b + 1) % n
        if b % n == 0:
            b += n
        if b not in a:
            a.append(b)
    else:
        break

print(' '.join(map(str, a))) if len(a) == n else print('Impossible')
