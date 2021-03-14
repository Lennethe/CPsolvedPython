import sys
from collections import deque

inputs = deque()
for inp in sys.stdin:
    inputs.append(inp.rstrip('\r\n'))

N, S, D = [int(x) for x in inputs.popleft().split()]

ans = "No"
for i in range(N):
    X, Y = [int(x) for x in inputs.popleft().split()]
    if X < S and D < Y:
        ans = "Yes"

print(ans)
