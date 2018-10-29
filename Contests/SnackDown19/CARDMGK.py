# # from collections import deque
# #
# #
# # def leftRot(a,A):
# #     b = a.popleft()
# #     a.append(b)
# #     if list(a) == A:
# #         return True
# #
# #
# # t = int(input())
# # while t > 0:
# #     n = int(input())
# #     flag = 0
# #     a = deque(map(int, input().split()))
# #     A = list(a)
# #     A.sort()
# #     d = 1
# #     while d != n+1:
# #         if not leftRot(a,A):
# #             d += 1
# #         else:
# #             print("YES")
# #             flag = 1
# #             break
# #     if flag != 1:
# #         print("NO")
# #     t -= 1
#

# t = int(input())
# while t > 0:
#     n = int(input())
#     a = list(map(int, input().split()))
#     A = [i for i in a]
#     flag = False
#     A.sort()
#     k = 0
#     b = []
#     while k <= n:
#         if a == A or b == A:
#             flag = True
#             break
#         else:
#             b = a[k:] + a[:k]
#             k += 1
#     if flag:
#         print("YES")
#     else:
#         print("NO")
#     t -= 1

t = int(input())
while t > 0:
    n = int(input())
    flag = False
    a = list(map(int, input().split()))
    A = [i for i in a]
    A.sort()
    pos=neg=0
    negpos=-1
    for i in range(n-1):
        if a[i+1]-a[i]>=0:
            pos+=1
        else:
            neg+=1
            negpos=i
            if neg>1:
                break
                flag = True

    # print(pos,neg)
    # print(a)
    b=a[negpos+1:] + a[:negpos+1]
    # print(b)
    if  b== A and not flag:
        print("YES")
    else:
        print("NO")
    t-=1
