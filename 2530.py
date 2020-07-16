word = input()

s = [word]

for letters in ['TK', 'DG', 'LR', 'FR']:
##    print(letters)
    for new_word in s:
        for k in range(word.count(letters[0])):
            replaced = new_word.replace(letters[0], letters[1], k + 1)
##            print(new_word, replaced, s)
            if replaced not in s:
                s.append(replaced)

print(s)
print(len(s))
