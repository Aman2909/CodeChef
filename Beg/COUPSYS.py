t=int(input())
while t>0:
    B=[[[],[]],[[],[]],[[],[]]]
    n=int(input())
    for i in range(n):
        c,l,x=map(int,input().split())
        B[l-1][0].append(x)
        B[l-1][1].append(c)
    for i in range(3):
        y=max(B[i][0])
        C=[j for j, x in enumerate(B[i][0]) if x==y]
        top = 101
        for k in range(len(C)):
            if B[i][1][C[k]]<top:
                top=B[i][1][C[k]]
        print(y,top)
    t-=1
