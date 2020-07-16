n, m , k = map(int, input().split())
l = [list(map(int, input().split())) for i in range(k)]

if k % 2 == 1:
    print(0)
elif k >= n * m:
    print(-1)
else:
    print(1)
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [i, j] not in l:
                print(i, j)
                break
        if [i, j] not in l:
            break

