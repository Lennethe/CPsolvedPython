from sys import stdin

H, W = [int(x) for x in stdin.readline().rstrip().split()]
YX = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(H)]
min_x = (min(sum(YX, [])))
ans = 0
for h in range(H):
    for w in range(W):
        ans += YX[h][w] - min_x
print(ans)
