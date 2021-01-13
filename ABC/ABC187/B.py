from sys import stdin

n = int(stdin.readline().rstrip())
v2 = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(i+1, n):
        x = abs(v2[j][0] - v2[i][0])
        y = abs(v2[j][1] - v2[i][1])
        if x >= y:
            ans += 1

print(ans)