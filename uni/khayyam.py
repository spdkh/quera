n = int(input())

line = [1]
print(1)

if n > 1:
    new_line = [1,1]
    line = new_line[:]
    print(1, 1)
    for i in range(2, n):
        new_line.insert(1, 1 + line[1])
        for j in range(2, i):
            new_line[j] = line[j - 1] + line[j]
        line = new_line[:]
        
        print(' '.join(list(map(str, new_line))))
