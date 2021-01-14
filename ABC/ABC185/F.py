from sys import stdin


# 1-indexed
class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.lst = [0] * n

    def add(self, i, w):
        while i <= self.n:
            self.lst[i-1] ^= w
            i += i & (-i)
        return

    def sum(self, i):
        res = 0
        while i > 0:
            res ^= self.lst[i-1]
            i -= i & (-i)
        return res


N, Q = [int(x) for x in stdin.readline().rstrip().split()]
BIT = BinaryIndexedTree(N)

A = [int(x) for x in stdin.readline().rstrip().split()]
for i, w in enumerate(A):
    BIT.add(i+1, w)

for i in range(Q):
    T, X, Y = [int(x) for x in stdin.readline().rstrip().split()]
    if T == 2:
        print(BIT.sum(Y) ^ BIT.sum(X-1))
    if T == 1:
        BIT.add(X, Y)
