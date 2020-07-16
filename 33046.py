n = int(input())

v, u = zip(* [map(int,input().split()) for i in range(n - 1)]) if n != 1 else [0,0]

_max = 0

for i in range(1, n):
	color = v.count(i) + u.count(i)

	if color > _max:
		_max = color

print(_max)