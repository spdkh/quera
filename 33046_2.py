n = int(input())

color = [0] * n

for i in range(n - 1):
	u, v = map(int,input().split())

	color[u - 1] += 1
	color[v - 1] += 1

print(max(color))