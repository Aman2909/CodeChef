A = ['f', 'r', 'i', 'e', 'z', 'a']
t = int(input())

while t > 0:
    good, bad, flag = 0, 0, 0
    s = list(input())
    if A.__contains__(s[0]):
        good = 1
    else:
        bad = 1
    print(s)
    for x in range(1, len(s)):
        if A.__contains__(s[x]):
            good += 1
            flag = 0
        else:
            bad += 1
            flag = 1
        if good != 0 and bad != 0:
            if flag == 0:
                print(bad, end=' ')
                bad=0
            else:
                print(good, end=' ')
                good=0
    if good!=0:
        print(good)
    if bad!=0:
        print(bad)
    t -= 1
