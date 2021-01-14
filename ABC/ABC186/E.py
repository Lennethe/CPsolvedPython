from sys import stdin


# 拡張ユークリッド互除法
# gcd(a,b) と ax + by = gcd(a,b) の最小整数解を返す
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


# mを法とするaの乗法的逆元
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        print(2222)
        raise Exception('modular inverse does not exist')
    else:
        return x % m


# Ax ≡ B mod M を満たす最小のxを導く
def solve(A, B, M):
    d, _, _ = egcd(A, egcd(B, M)[0])
    A //= d
    B //= d
    M //= d
    if egcd(A, M)[0] != 1:
        return -1
    else:
        return modinv(A, M) * B % M


T = int(stdin.readline().rstrip())

for i in range(T):
    N, S, K = [int(x) for x in stdin.readline().rstrip().split()]
    print(solve(K, (-S+N*S) % N, N))
