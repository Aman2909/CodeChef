#28th june
t= int(input())
while t>0:
    x=input()
    y=input()
    for i,j in zip(x,y):
        if i==j:
            if i=='B':
                print('W',end='')
            else: print('B',end='')
        else:
            print('B', end='')
    print(end='\n')
    t-=1