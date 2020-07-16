n = int(input())
color = list(map(int,input().split()))

# print(color)
minim = color.count(color[0])
idx = color[0]

for i in color:
	# print(i, minim, idx)
	if color.count(i) < minim:
		minim = color.count(i)
		idx = i
	elif color.count(i) == minim:
		idx = min(i,idx)

print(idx)
