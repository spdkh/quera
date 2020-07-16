n, m = map(int, input().split())

q,a = zip(*[map(str, input().split()) for i in range(n)])
words = list(map(str, input().split())) 
for i in words:
    if i in q:
        print(a[q.index(i)], end = ' ')
    print('kachal!', end = ' ')
