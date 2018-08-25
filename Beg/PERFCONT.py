t = int(input())
for i in range(t):
    h, c = 0, 0
    n, p = map(int, input().split())
    num = list(map(int, input().split()))
    for j in range(n):
        z = num[j]
        if z <= p // 10:
            h = h + 1
        elif z >= p // 2:
            c = c + 1
    if h == 2 and c == 1:
        print("yes")
    else:
        print("no")
