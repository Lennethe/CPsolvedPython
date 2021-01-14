import math


class segki():
    # modeで関数を選べます。(min,max,sum,prd(product),gcd,lmc,^,&,|)
    # 葉の数N,要素ls
    def __init__(self, N, ls, mode='min'):
        self.mode = mode
        self.default = self.setdef()
        self.N = N
        self.K = (N-1).bit_length()
        self.N2 = 1 << self.K
        self.dat = [self.default]*(2**(self.K+1))
        # 葉の構築
        for i in range(self.N): 
            self.dat[self.N2+i] = ls[i]
        self.build()

    # 単位元を設定
    def setdef(self):
        if self.mode == 'min':
            return 1 << 60
        elif self.mode == 'max':
            return -(1 << 60)
        elif self.mode == 'sum':
            return 0
        elif self.mode == 'prd':
            return 1
        elif self.mode == 'gcd':
            return 0
        elif self.mode == 'lmc':
            return 1
        elif self.mode == '^':
            return 0
        elif self.mode == '&':
            return (1 << 60)-1
        elif self.mode == '|':
            return 0

    def build(self):
        for j in range(self.N2-1, -1, -1):
            # 親が持つ条件
            self.dat[j] = self.func(self.dat[j << 1], self.dat[j << 1 | 1])

    # 関数を指定
    def func(self, x, y):
        if self.mode == 'min':
            return min(x, y)
        elif self.mode == 'max':
            return max(x, y)
        elif self.mode == 'sum':
            return x+y
        elif self.mode == 'prd':
            return x*y
        elif self.mode == 'gcd':
            return math.gcd(x, y)
        elif self.mode == 'lmc':
            return (x*y)//math.gcd(x, y)
        elif self.mode == '^':
            return x ^ y
        elif self.mode == '&':
            return x & y
        elif self.mode == '|':
            return x | y

    # リストのx番目の値
    def leafvalue(self, x):
        return self.dat[x+self.N2]

    # index(x)をyに変更
    def update(self, x, y):
        i = x+self.N2
        self.dat[i] = y
        # 親の値を変更
        while (i > 0):
            i >>= 1
            self.dat[i] = self.func(self.dat[i << 1], self.dat[i << 1 | 1])
        return

    def query(self, L, R):  # [L,R)の区間取得
        L += self.N2
        R += self.N2
        vL = self.default
        vR = self.default
        while L < R:
            if L & 1:
                vL = self.func(vL, self.dat[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.func(self.dat[R], vR)
            L >>= 1
            R >>= 1
        return self.func(vL, vR)
