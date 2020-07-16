n, m = map(int, input().split())
l, r = zip(* [map(int, input().split()) for i in range(n + m)])

a = set()
b = set()
for i in range(n):
	a.update(range(l[i], r[i] + 1))

for i in range(n, n + m):
	b.update(range(l[i], r[i] + 1))

print(len(a.intersection(b)))