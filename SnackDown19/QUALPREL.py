t=int(input())
while t>0:
    n,k=map(int,input().split())
    count = k
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    b=a[k-1]
    for i in range(k,n):
        if a[i] == b: count+=1
        else: break
    print(count)
    t-=1