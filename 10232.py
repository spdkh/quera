n, l = map(int, input().split())
d, r, g = zip(* [map(int, input().split()) for i in range(n)])

t = l
r_ = [(r[0] - d[0] + g[0]) % (r[0] + g[0])]
r_[0] = 0 if r_[0] == 0 else r_[0] - g[0] + 1
for i in range(1, n):
	r_.append((r[i] - (sum(r_) + d[i]) + g[i]) % (r[i] + g[i]))

t += sum(r_)
print(t)