from sys import stdin
from functools import lru_cache


@lru_cache(maxsize=None)
def solve(x, y):
    if y == 1:
        return abs(x-y)
    elif y % 2 == 1:
        return min(abs(x-y), solve(x, (y+1)//2) + 2, solve(x, (y-1)//2) + 2)
    else:
        return min(abs(x-y), solve(x, y//2) + 1)


x, y = [int(x) for x in stdin.readline().rstrip().split()]

print(solve(x, y))
