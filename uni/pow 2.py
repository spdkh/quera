n = int(input())

cnt = 0
while n >= 1:
##    print(n)
    n /= 2
    cnt += 1

print(2 ** cnt)
