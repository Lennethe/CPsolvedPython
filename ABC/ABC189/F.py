from sys import stdin

n,m,k=[int(x) for x in stdin.readline().rstrip().split()]
A=[int(x) for x in stdin.readline().rstrip().split()]
l=n+m+1
a,b=[0]*l,[0]*l
for i in A: a[i]=1
s=t=0
for i in range(n)[::-1]:
    print(i, s, t)
    if a[i]<1: a[i],b[i]=s/m,t/m+1
    s+=a[i]-a[i+m]
    t+=b[i]-b[i+m]
print("a", a)
print("b", b)
print(b[0]/(1-a[0]) if 1-a[0]>1e-9 else -1)