import time

n, W = map(int, input().split())
w = list(map(int, input().split()))
start = time.time()
maxim = 0
for i in range(n):
    for j in range(i + 1, n + 1):
        a = sum(w[:j]) - sum(w[:i])
        if a <= W and  maxim < a:
            maxim = a
##        print(a, sum(a), maxim)
print(maxim)
print(time.time() - start)
