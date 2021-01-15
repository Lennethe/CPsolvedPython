from sys import stdin


N, M = [int(x) for x in stdin.readline().rstrip().split()]
S = stdin.readline().rstrip()

for s in S:
    if s == 'o':
        M += 1
    else:
        M = max(0, M-1)
print(M)
