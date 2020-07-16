n = int(input())

cnd = int(input())
cnt = 0
for i in range(n - 1):
    a = int(input())
    if cnd != a:
        cnt += 1
    cnd = a

print(cnt)
