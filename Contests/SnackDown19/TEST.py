def array_left_rotation(a, n, k):
    a=a[k:]+a[:k]
    return a
# or by this way
def array_left_rotation1(a, n, k):
  return [a[(k+i)%n] for i in range(n)]

a=[4,5,1,2,3]
n=5
k=2
b=array_left_rotation(a,n,k)
print(b)