s = [input() for i in range(7)]

c = 0
for i in range(7):
	for j in range(7):
		if i > 1:
			if s[i - 2][j] == '.' and s[i - 1][j] == 'o' and s[i][j] == 'o':
				c += 1
		if j > 1:
			if s[i][j - 2] == '.' and s[i][j - 1] == 'o' and s[i][j]	== 'o': 
				c += 1
		if i < 5:
			if s[i + 2][j] == '.' and s[i + 1][j] == 'o' and s[i][j] == 'o': 
				c += 1
		if j < 5:
			if s[i][j + 2] == '.' and s[i][j + 1] == 'o' and s[i][j] == 'o':
				c += 1

print(c)