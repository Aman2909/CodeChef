# Pari and Prime

t = int(input())
modulo = 10**9 + 7
while t>0:
    l,r = map(int,input().split())
    sumfacs=0

    for n in range(l,r+1):
        facs=[]
        last=n//2
        prime=True

        for i in range(2,last+1):
            if n%i==0 and i not in facs:
                prime=False
                facs.append(i)
        if prime:
            facs.append(n)

        sumfacs+=sum(facs)
    t-=1