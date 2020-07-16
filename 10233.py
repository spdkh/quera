def check2(x):
	x = ''.join(x)
	minim = max(map(int, x))
	
	for i in x[1:]:
		if int(i) < minim and int(i) >= int(x[0]):
			minim = int(i)
	minim = str(minim)

	x = x.replace(minim, x[0], 1)
	x = x.replace(x[0], minim, 1)

	y = list(x[1:])
	y.sort()
	y = ''.join(y)

	return x[0]+y
	
def check(x):
	y = list(x[:])
	x = list(x)
	x.sort()
	x.reverse()

	if x == y:
		return '0'

	if len(y) == 2:
		y = list(y)
		y.reverse()
		y = ''.join(y)
		return y

	if check(y[1:]) == '0':
		return check2(y)

	y = ''.join(y)
	return y[0]+check(y[1:])
	
s = input()
print(check(s))