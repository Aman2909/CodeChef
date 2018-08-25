t=int(input())
while t>0:
    n=int(input())
    A=list(map(int,input().split()))
    y=sum(A)
    if y%2==0: print("NO")
    else: print("YES")
    t-=1
