shoulderxl, heightxl = map(int, input().split())
shoulderw, heightw = map(int, input().split())

if shoulderxl >= shoulderw and heightxl >= heightw:
	print('yes')
else:
	print('no')
