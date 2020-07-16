def bmm(n, m):
    o = 1
    minimum = min(n,m)
    maximum = max(n,m)
    for i in range(1, minimum // 2 + 1):
        if minimum % i == 0:
            if maximum % (minimum // i) == 0:
                o = minimum // i
                break
    return o

def kmm(n, m):
    o = n * m
    minimum = min(n,m)
    maximum = max(n,m)
    i = 1
    for i in range(1, minimum // 2 + 1):
        if minimum % i == 0:
            if(maximum * i) % minimum == 0:
                o = i * maximum
                break
    return o
n,m = map(int, input().split())

print(bmm(n, m), kmm(n, m))
