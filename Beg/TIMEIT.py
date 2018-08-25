t=int(input())
for I in range(t):
    n=int(input())
    if(360%n==0):
        print('y',end=' ')
    else:
        print('n',end=' ')
    if(n<=360):
        print('y',end=' ')
    else:
        print('n',end=' ')
    if(n<27):
        print('y')
    else:
        print('n')