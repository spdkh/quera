p,d = map(int,input().split())

i = 0
while True:
    i += d
    x = i % p
    if x <= p / 2 and x >= 0:
        break

print(i)
