from sys import stdin
from collections import defaultdict


class UnionFindVerSize():
    def __init__(self, N):
        """ N個のノードのUnion-Find木を作成する """
        # 親の番号を格納する。自分が親だった場合は、自分の番号になり、それがそのグループの番号になる
        self._parent = [n for n in range(0, N)]
        # グループのサイズ（個数）
        self._size = [1] * N

    def find_root(self, x):
        """ xの木の根(xがどのグループか)を求める """
        if self._parent[x] == x:
            return x
        # 縮約
        self._parent[x] = self.find_root(self._parent[x])
        return self._parent[x]

    def unite(self, x, y):
        """ xとyの属するグループを併合する """
        gx = self.find_root(x)
        gy = self.find_root(y)
        if gx == gy:
            return

        # 小さい方を大きい方に併合させる（木の偏りが減るので）
        if self._size[gx] < self._size[gy]:
            self._parent[gx] = gy
            self._size[gy] += self._size[gx]
        else:
            self._parent[gy] = gx
            self._size[gx] += self._size[gy]

    def get_size(self, x):
        """ xが属するグループのサイズ（個数）を返す """
        return self._size[self.find_root(x)]

    def is_same_group(self, x, y):
        """ xとyが同じ集合に属するか否か """
        return self.find_root(x) == self.find_root(y)

    def calc_group_num(self):
        """ グループ数を計算して返す """
        N = len(self._parent)
        ans = 0
        for i in range(N):
            if self.find_root(i) == i:
                ans += 1
        return ans


N, Q = [int(x) for x in stdin.readline().rstrip().split()]
C = [int(x) for x in stdin.readline().rstrip().split()]
UF = UnionFindVerSize(N+1)
res = [defaultdict(int) for a in range(N+1)]
for i, c in enumerate(C, 1):
    res[i][c] = 1


for i in range(Q):
    T, A, B = [int(x) for x in stdin.readline().rstrip().split()]
    if T == 1:
        A_root = UF.find_root(A)
        B_root = UF.find_root(B)
        if A_root == B_root:
            continue
        UF.unite(A, B)
        if len(res[A_root]) > len(res[B_root]):
            res[A_root], res[B_root] = res[B_root], res[A_root]
        for key, value in res[A_root].items():
            res[B_root][key] += value
        res[A_root] = res[B_root]
    else:
        A_root = UF.find_root(A)
        print(res[A_root][B])
