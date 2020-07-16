n, l = map(int, input().split())
d, r, g = zip(* [map(int, input().split()) for i in range(n)])

r_left = [(list(range(r[i], 0, -1))+ [0] * g[i]) for i in range(n)]
##print(r_left)

t = 0
for i in range(n):
	r_left[i] = ((t + d[i]) // len(r_left[i]) + 1) * r_left[i]
	t += d[i] if i == 0 else d[i] - d[i - 1]
##	print('test:', r_left[i][t])
	t += r_left[i][t]
##	print(len(r_left[i]), d[i], t)
t += l - d[n - 1]
print(t)
