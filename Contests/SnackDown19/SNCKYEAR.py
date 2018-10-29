# Chef and SnackDown
# 2010, 2015, 2016, 2017 and 2019.

t=int(input())
dict = {
    "2010":"HOSTED",
    "2015":"HOSTED",
    "2016":"HOSTED",
    "2017":"HOSTED",
    "2019":"HOSTED"
}
while t>0:
    year = input()
    if year in dict:
        print(dict[year])
    else:
        print("NOT HOSTED")
    t-=1
