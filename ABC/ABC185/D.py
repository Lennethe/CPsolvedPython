from sys import stdin
import math

N, M = [int(x) for x in stdin.readline().rstrip().split()]
if M == 0:
    print(1)
    exit()

V = [0] + sorted([int(x) for x in stdin.readline().rstrip().split()]) + [N+1]


x = 1e9
ans = 0
for i in range(1, M+1):
    if V[i] - V[i-1] - 1 > 0:
        x = min(x, V[i] - V[i-1] - 1)

for i in range(1, M+2):
    ans += math.ceil((V[i] - V[i-1] - 1)/x)

print(ans)
