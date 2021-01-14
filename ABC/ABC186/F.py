from sys import stdin
from collections import deque


# 1-indexed
class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.lst = [0] * n

    def add(self, i, w):
        while i <= self.n:
            self.lst[i-1] += w
            i += i & (-i)
        return

    def sum(self, i):
        res = 0
        while i > 0:
            res += self.lst[i-1]
            i -= i & (-i)
        return res


H, W, M = [int(x) for x in stdin.readline().rstrip().split()]
h_min = [H] * (W + 1)
w_min = [W] * (H + 1)

for i in range(M):
    Y, X = [int(x) for x in stdin.readline().rstrip().split()]
    h_min[X] = min(h_min[X], Y-1)
    w_min[Y] = min(w_min[Y], X-1)

ans = 0
block = []
for x in range(1, w_min[1]+1):
    ans += h_min[x]
    block.append([h_min[x] + 1, x])

BIT = BinaryIndexedTree(W)
que = deque(sorted(block))

for x in range(w_min[1]+1, W+1):
    BIT.add(x, 1)

for y in range(2, h_min[1]+1):
    while que and que[0][0] < y:
        block_y, block_x = que.popleft()
        BIT.add(block_x, 1)
    ans += BIT.sum(w_min[y])

print(ans)
