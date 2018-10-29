t = int(input())
modulus = 1000000007
while t>0:
    n,k=map(int,input().split())
    best=[]
    pro=1
    no=done = False
    div=n//k
    best=[i for i in range(div-k//2,div+1+k//2)]

    if k==2 and n%2!=0:
        best.remove(div-1)
        if 0 in best:
            no = True
        for i in best:
            pro *= i**2-i
        done = True



    if not done:
        if k%2==0 :
            best.remove(div)


        if n%k!=0:
            for i in range(k-1,k-(n%k)-1,-1):
                best[i] += 1
        # if sum(best)!= n:
        #     best
        if 0 in best:
            no = True
        else:
            for i in best:
                pro *= i**2-i

    if not no:
        pro=pro%modulus
        print(pro)
    else:
        print(-1)
    t-=1