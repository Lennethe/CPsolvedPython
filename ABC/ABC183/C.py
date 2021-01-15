from sys import stdin
import itertools

N, K = [int(x) for x in stdin.readline().rstrip().split()]
v2 = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(N)]

x = list(range(2, N+1))
ans = 0
for lst in list(itertools.permutations(x)):
    here = 1
    cst = 0
    for there in lst:
        cst += v2[here-1][there-1]
        here = there
    cst += v2[there-1][0]
    if cst == K:
        ans += 1

print(ans)
