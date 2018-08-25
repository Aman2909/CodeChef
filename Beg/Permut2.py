n = int(input())
while n!=0:
    A = list(map(int, input().split()))
    B=[0]*len(A)
    flag=0
    for i in range(n):
        B[A[i]-1]=i+1
    for i in range(n):
        if A[i] != B[i]:
            break
        else:
            flag += 1
    if flag == n:
        print("ambiguous")
    else:
        print("not ambiguous")
    n=int(input())
