r, c = map(int, input().split())

if c > 10:
    print('Left', 11 - r, 20 - c + 1)
else:
    print('Right', 11 - r, c)
