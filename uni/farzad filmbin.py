n = int(input())

s1 = [input().split() for i in range(n)]
s2 = [[] for i in range(n)]
for i in range(n):
##    print(s1[i])
    for word in s1[i]:
##        print(word)
        word = word[0].upper() + word[1:].lower()
        s2[i].extend(word+ ' ')

    print(''.join(s2[i]))
