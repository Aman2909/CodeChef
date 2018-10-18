t = int(input())
while t>0:
    n = int(input())
    a = list(map(int, input().split()))
    day,fstep,pstep,add=0,a[0],0,0
    while pstep<n:
        for i in range(pstep,fstep+1):
            try:
                add+=a[i]
            except:
                pass
        pstep=fstep+1
        fstep+=add
        day+=1
    print(day)
    t-=1
