t= int(input())
while t>0:
    n=int(input())

    if 360%n==0:
        print("y",end=' ')
    else:
        print("n",end=' ')

    if n<=360:
        print("y", end=' ')
    else:
        print("n", end=' ')

    if n<27:
        print("y",end='\n')
    else:
        print("n",end='\n')
    t-=1