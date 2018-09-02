def choice(a):
    if a==1: return 4,"LB"
    elif a==2: return 5,"MB"
    elif a==3: return 6,"UB"
    elif a==4: return 1,"LB"
    elif a==5: return 2,"MB"
    elif a==6: return 3,"UB"
    elif a==7: return 8,"SU"
    else: return -1,"SL"

t=int(input())
for i in range(t):
    num=int(input())
    x=num//8
    y=num%8
    y,label=choice(y)
    print(str(8*x+y)+label)