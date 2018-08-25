t = int(input())
while t > 0:
    n, a, b = map(float, input().split())
    pa, pb = 0, 0
    num = list(map(float, input().split()))
    for i in num:
        if a == i:
            pa = pa + 1
        if b == i:
            pb = pb + 1
    v = float(pa / n * pb / n)
    print("{0:.10f}".format(v))
    t = t - 1
