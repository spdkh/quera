def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

word = input()

letters =['TDLF', 'KGRR']
for l in word:
    if l not in letters[0]:
        word = word.replace(l, '')
        

print(2 ** len(word))
##
##n = [word.count(letters[0]) for letters in ['TK', 'DG', 'LR', 'FR']]
##n = list(filter(lambda x: x > 0, n))
##s = list(map(lambda x: fact(1+x), n))
##
##print(sum(s))
