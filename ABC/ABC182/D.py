from sys import stdin
from itertools import accumulate


N = int(stdin.readline().rstrip())
A = [0] + [int(x) for x in stdin.readline().rstrip().split()]
ACC = list(accumulate(A))
ACC2 = list(accumulate(ACC))
ans = 0
idx = 0
idxmax = 0

for i in range(1, N+1):
    if ACC[i] > idxmax:
        idx = i
        idxmax = ACC[i]
    ans = max(ans, ACC2[i-1] + ACC[idx])

print(ans)
