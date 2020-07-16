n = int(input())

a = list(map(int, input().split()))

max = 0
for i in range(n):
    for j in range(i + 1, n + 1):
##        print(a[i:j])
        s = sum(a[i:j])
        if s > max :
            max = s
  
print(max)
