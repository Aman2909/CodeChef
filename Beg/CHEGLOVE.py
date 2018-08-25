# t = int(input())
# while t>0:
#     n = int(input())
#     fig=list(map(int,input().split()))
#     sh=list(map(int,input().split()))
#     fflag,bflag,front,back=0,0,0,0
#     for x,y in zip(fig,sh):
#         if x<=y:
#             fflag+=1
#         else:
#             break
#
#     for x,z in zip(fig, reversed(sh)):
#         if x <= z:
#             bflag += 1
#         else:
#             break
#
#     if fflag==n:
#         front=1
#     if bflag==n:
#         back=1
#     if front==1:
#         if back==1:
#             print("both")
#         else:
#             print("front")
#     else:
#         if back==1:
#             print("back")
#         else:
#             print("none")
#     t-=1





t = int(input())
while t>0:
    n = int(input())
    fig=list(map(int,input().split()))
    sh=list(map(int,input().split()))
    fflag,bflag,front,back=0,0,0,0
    for x,y,z in zip(fig,sh,reversed(sh)):
        if x<=y:
            fflag+=1
        if x <= z:
            bflag += 1
        # else:
        #     break
    # for x,z in zip(fig, reversed(sh)):
    #     else:
    #         break

    if fflag==n:
        front=1
    if bflag==n:
        back=1
    if front==1:
        if back==1:
            print("both")
        else:
            print("front")
    else:
        if back==1:
            print("back")
        else:
            print("none")
    t-=1