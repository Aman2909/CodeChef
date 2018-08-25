t=int(input())
while t>0:
    n=int(input())
    loss=0
    for i in range(n):
        p,d,x=map(int,input().split())
        q=(p+p*x*0.01)
        q=(q-q*x*0.01)
        loss1=p-q
        loss=loss+loss1*d
    print("{0:.10f}".format(loss))
    t-=1