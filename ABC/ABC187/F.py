from sys import stdin

N, M = [int(x) for x in stdin.readline().rstrip().split()]
G = [1 << N] * N

for i in range(M):
    A, B = [int(x) for x in stdin.readline().rstrip().split()]
    A -= 1
    B -= 1
    G[A] |= 1 << B
    G[B] |= 1 << A

dp = [N] * (1 << N)
dp[0] = 1

for i in range(N):
    for j in range(1 << N):
        if dp[j] == 1 and (G[i] & j) == j:
            dp[j | 1 << i] = 1

for i in range(1 << N):
    j = i
    while j:
        if dp[i] > dp[i ^ j] + dp[j]:
            dp[i] = dp[i ^ j] + dp[j]
        j -= 1
        j &= i

print(dp[-1])
