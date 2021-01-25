from sys import stdin
from collections import defaultdict


def f(div, dif):
    X = dif//div
    Y = X
    if dif % div != 0:
        Y += 1
    return X, Y


N, G = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()] + [1e16]
A.reverse()

dp = []
for i in range(N+1):
    dp.append(defaultdict(int))

dp[0][0] = 1
for i in range(0, N):
    coin = A[i+1]
    for key in dp[i]:
        dif = G - key
        X, Y = f(coin, dif)
        if abs(coin*X) < A[i]:
            dp[i+1][key + coin*X] += dp[i][key]
        if X != Y and abs(coin*Y) < A[i]:
            dp[i+1][key + coin*Y] += dp[i][key]

print(dp[N][G])
