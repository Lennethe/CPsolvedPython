from sys import stdin
from itertools import accumulate

N = int(stdin.readline().rstrip())
V = [0] + sorted([int(x) for x in stdin.readline().rstrip().split()])
ACC_V = list(accumulate(V))

ans = 0
for i in range(1, N):
    ans += ACC_V[-1] - ACC_V[i] - (N - i) * V[i]
print(ans)
