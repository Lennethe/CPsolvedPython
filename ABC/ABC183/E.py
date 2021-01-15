from sys import stdin


H, W = [int(x) for x in stdin.readline().rstrip().split()]
mp = [stdin.readline().rstrip() for _ in range(H)]

dp = [([0] * W) for _ in range(H)]
dp_r = [([0] * W) for _ in range(H)]
dp_d = [([0] * W) for _ in range(H)]
dp_rd = [([0] * W) for _ in range(H)]

dp[0][0] = 1
dp_r[0][0] = 1
dp_d[0][0] = 1
dp_rd[0][0] = 1

MOV = [[-1, 0], [-1, -1], [0, -1]]
MOD = 1000000007
for y in range(H):
    for x in range(W):
        if mp[y][x] == "#":
            continue
        if x > 0:
            dp[y][x] += dp_r[y][x-1]
        if y > 0:
            dp[y][x] += dp_d[y-1][x]
        if x * y > 0:
            dp[y][x] += dp_rd[y-1][x-1]
        dp_r[y][x] = dp[y][x]
        dp_d[y][x] = dp[y][x]
        dp_rd[y][x] = dp[y][x]
        if x > 0:
            dp_r[y][x] = dp[y][x] + dp_r[y][x-1]
        if y > 0:
            dp_d[y][x] = dp[y][x] + dp_d[y-1][x]
        if x * y > 0:
            dp_rd[y][x] = dp[y][x] + dp_rd[y-1][x-1]
        dp[y][x] %= MOD
        dp_r[y][x] %= MOD
        dp_d[y][x] %= MOD
        dp_rd[y][x] %= MOD

print(dp[H-1][W-1])
