import math
n = int(input())
word = input()
s, t = map(int, input().split())

word = word[min(s,t) - 1: max(s, t)]

c = 0
for i in range(int(math.ceil(math.log2(len(word)))), -1, -1):
##    print(int(2 ** i) * 'H')
    c += word.count(2 ** i * 'H')
    word = word.replace(2 ** i * 'H', '')

print(c)
