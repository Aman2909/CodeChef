t = int(input())
while t > 0:
    count=0
    n = int(input())
    A=list(map(int,input().split()))
    for i in range(n):
        count=count^2*A[i]
    print(count)
    t = t - 1
