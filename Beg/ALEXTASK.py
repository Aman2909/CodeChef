def gcd(m,n):
    while(n!=0):
        r=m%n
        m=n
        n=r
    return m

t = int(input())
while t > 0:
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    k=gcd(A[0],A[1])
    k=A[0]*A[1]//k
    #  for i in range (n):
    #     for j in range (i+1,n):
    #         k = lcm(A[0], A[1])
    print(k)
    t -= 1

