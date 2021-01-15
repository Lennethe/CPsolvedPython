from sys import stdin
from collections import deque


A, B, C = [int(x) for x in stdin.readline().rstrip().split()]

dp = [[([0] * 101) for a in range(101)] for b in range(101)]
que = deque([(A, B, C)])
dp[A][B][C] = 1

while que:
    x, y, z = que.popleft()
    if x >= 100 or y >= 100 or z >= 100:
        continue
    if 0 < x < 100:
        if dp[x+1][y][z] == 0:
            que.append([x+1, y, z])
        dp[x+1][y][z] += dp[x][y][z] * x/(x+y+z)
    if 0 < y < 100:
        if dp[x][y+1][z] == 0:
            que.append([x, y+1, z])
        dp[x][y+1][z] += dp[x][y][z] * y/(x+y+z)
    if 0 < z < 100:
        if dp[x][y][z+1] == 0:
            que.append([x, y, z+1])
        dp[x][y][z+1] += dp[x][y][z] * z/(x+y+z)

ans = 0
for i in range(100):
    for j in range(100):
        ans += (dp[100][i][j] + dp[i][100][j] + dp[i][j][100]) * (100+i+j - A-B-C)
print(ans)
