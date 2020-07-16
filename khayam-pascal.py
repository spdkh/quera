def fact(i):
    if i == 0 or i == 1:
        return 1
    return i * fact(i-1)
    
n = int(input())


for i in range(n):
    for j in range(i+1):

        print(int(fact(i)/(fact(j)*fact(i-j))), end = ' ')
    print()
