from sys import stdin
import bisect


N, T = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()]

X = set()
X.add(0)
for a in A[:len(A)//2]:
    keys = list(X)
    for k in keys:
        X.add(k+a)

Y = set()
Y.add(0)
for a in A[len(A)//2:]:
    keys = list(Y)
    for k in keys:
        Y.add(k+a)

X = sorted(X)
Y = sorted(Y)

ans = 0
for x in X:
    if x > T:
        continue
    idx = bisect.bisect(Y, max(0, T-x))
    ans = max(ans, Y[idx-1] + x)

print(ans)
