# Ego stone
t = int(input())
while t>0:
    n=int(input())
    if n%2==0:
        result=(n*((n ** 2)+1))/2
    else:
        result= n*(((n ** 2)+1)/2)
    print('%.0f'%result)
    t-=1