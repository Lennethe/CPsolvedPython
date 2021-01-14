from sys import stdin

N, M = [int(x) for x in stdin.readline().rstrip().split()]
A = [0] + [int(x) for x in stdin.readline().rstrip().split()] + [0]
B = [0] + [int(x) for x in stdin.readline().rstrip().split()] + [0]

dp = [([1e9] * (N+2)) for i in range(M+2)]
dp[0][0] = 0

for i in range(N+1):
    for j in range(M+1):
        if A[i+1] == B[j+1]:
            dp[j+1][i+1] = min(dp[j][i], dp[j+1][i+1])
        if A[i+1] != B[j+1]:
            dp[j+1][i+1] = min(dp[j][i]+1, dp[j+1][i+1])
        dp[j+1][i] = min(dp[j][i] + 1, dp[j+1][i])
        dp[j][i+1] = min(dp[j][i] + 1, dp[j][i+1])


print(dp[M][N])
