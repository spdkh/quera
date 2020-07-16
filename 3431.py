n, m = list(map(int, input().split()))

s = 0
c = 0
words = [input() for i in range(n + 1)]
words2 = list(map(list, zip(*words[:n])))
for i in range(n):
    
    while words[n] in words[i]:
        s = words[i].index(words[n])
        words[i] = words[i].replace(words[i][s], '*', 1)
##        print(s, words[i])
        c += 1
for i in range(m):
    words2[i] = ''.join(words2[i])
    while words[n] in words2[i]:
        s = words2[i].index(words[n])
        words2[i] = words2[i].replace(words2[i][s], '*', 1)
##        print(s, words2[i])
        c += 1
        
print(c)
