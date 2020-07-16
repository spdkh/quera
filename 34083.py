q = int(input())

ip = []
user = []
money = []

for i in range(q):
    t, word = map(str, input().split())
    t = int(t)
    word = word.split(':')
    
    if t == 1:
        if '_' in word[1] or '*' in word[1] or '#' in word[1] or '$' in word[1]:
            print('invalid username')
        else:
            ip.append(word[0])
            user.append(word[1])
            money.append(0)

    elif t == 2:
        money[user.index(word[1])] += int(word[2]) 
        money[ip.index(word[0])] -= int(word[2])
    else:
        print(money[ip.index(word[0])])


