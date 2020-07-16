n, k = list(map(int, input().split()))

c = [int(input()) for i in range(n)]
if sum(c) >= k:
    print('YES')
else:
    print('NO')
