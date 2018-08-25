n=int(input())
A=list(map(int,input().split()))
B=[0 for p in range(n)]
for x,y in zip(A,range(n)):
    if y+1 in A:
        B[y]=1
for x in range(n):
    if B[x]==0:
        print(x+1, end=" ")