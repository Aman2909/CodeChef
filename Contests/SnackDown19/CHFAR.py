t=int(input())
while t>0:
    n,k = map(int,input().split())
    a=list(map(int,input().split()))
    if n-a.count(1)<=k:
        print("YES")
    else:
        print("NO")
    t-=1