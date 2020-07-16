import time
n, W = map(int, input().split())
w = list(map(int, input().split()))
start = time.time()
maxim = 0
for i in range(n):
    for j in range(i + 1, n + 1):
        a = w[i: j]
        if sum(a) <= W and  maxim < sum(a):
            maxim = sum(a)
##        print(a, sum(a), maxim)
print(maxim)
print(time.time() - start)
