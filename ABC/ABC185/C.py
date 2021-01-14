from sys import stdin
import math


def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


N = int(stdin.readline().rstrip())

print(comb(N-1, 11))