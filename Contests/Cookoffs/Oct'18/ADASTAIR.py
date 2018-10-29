t = int(input())
while t>0:
    n,k = map(int,input().split())
    count,a =0,list(map(int,input().split()))
    for i in range(1,n):
        diff=a[i] - a[i-1]
        if diff>= k:
            count += diff//k
    print(count)
    t-=1