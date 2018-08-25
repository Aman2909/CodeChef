t= int (input())
while t>0:
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    A.sort()
    B.sort()
    y=sum(A)-A[n-1]
    z=sum(B)-B[n-1]
    if y<z: print("Alice")
    elif z<y : print("Bob")
    else: print("Draw")
    t-=1
