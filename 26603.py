n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = [a[i] * b[i] for i in range(n)]
print(sum(c))