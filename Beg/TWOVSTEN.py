t= int (input())
while t>0:
    n=int(input())
    x=n%10
    if(x==0): print("0")
    elif (x==5): print("1")
    else: print("-1")
    t-=1