t = int(input())
while t>0:
    n,q=map(int,input().split())
    carrots=list(map(int,input().split()))
    for i in range(q):
        k=int(input())
        ans=0
        for i in range(0,n,k+1):
            ans+=carrots[i]
        # ans=sum(carrots[0::k + 1])
        print(ans)
    t-=1