n = int(input())
ones = 0
A = [[0 for x in range(n + 1)] for y in range(n + 1)]
for x in range(n):
    l, r = map(int, input().split())
    for y in range(l - 1, r):
        A[x][y] = 1
    ones = ones + (r-l+1)
    A[x][n] = r-l+1
for y in range(n):
    tempone = 0
    for x in range(n):
        if A[x][y] == 1:
            tempone += 1
    A[n][y] = tempone
q = int(input())
for i in range(q):
    qr, qc = map(int, input().split())
    sum = A[qr - 1][n] + A[n][qc - 1]
    if A[qr - 1][qc - 1] == 1:
        sum = ones - sum + 1
    else:
        sum = ones - sum
    if sum % 2 == 0:
        print("E")
    else:
        print("O")


# Testing this for git- New branch code. :)
#Remote to Local
