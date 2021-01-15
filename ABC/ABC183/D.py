from sys import stdin
from itertools import accumulate


N, M = [int(x) for x in stdin.readline().rstrip().split()]

dp = [0] * 300000

for i in range(N):
    S, T, P = [int(x) for x in stdin.readline().rstrip().split()]
    dp[S] += P
    dp[T] -= P

if max(accumulate(dp)) <= M:
    print("Yes")
else:
    print("No")