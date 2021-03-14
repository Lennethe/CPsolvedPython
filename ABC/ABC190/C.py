import sys
from itertools import product
from collections import deque

inputs = deque()
for inp in sys.stdin:
    inputs.append(inp.rstrip('\r\n'))


N, M = [int(x) for x in inputs.popleft().split()]
dishes = [[int(x) for x in inputs.popleft().split()] for a in range(M)]
K = int(inputs.popleft())
choices = [[int(x) for x in inputs.popleft().split()] for a in range(K)]

cnt = 0
for balls in product(*choices):
    balls = set(balls)
    cnt = max(cnt, sum([A in balls and B in balls for A, B in dishes]))
print(cnt)
