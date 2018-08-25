B=[[0] for x in range(32)]
print(B)
A=list(map(int,input().split()))
for x in A:
    digit=0
    y = bin(x)[2::]
    e=int(y)
    while e>0:
        digit+=1
        e//=10
    B[digit].append(x)
print(B)
for x in range(32):
    digit = 0
    for y in B[x]:
        digit=digit^y
    print(digit)
    B[x][0]=digit
print(B)