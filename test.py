n = 3
s = 1
a = 2
d = 3
# print("MOVE FROM", s, "to", d)
def tower(s,a,d,n):
    if n==1:
        print("MOVE FROM", s ,"TO" ,d)
    else:
        tower(s,d,a,n-1)
        tower(s,a,d,1)
        tower(a,s,d,n-1)

tower(s,a,d,n)
