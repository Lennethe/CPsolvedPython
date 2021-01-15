from sys import stdin
from collections import defaultdict, deque
import string


H, W = [int(x) for x in stdin.readline().rstrip().split()]
V = []
tereport = defaultdict(list)

start = (0, 0)
goal = (0, 0)
used_g = [([1e9] * W) for _ in range(H)]
for h in range(H):
    S = stdin.readline().rstrip()
    V.append(S)
    for w, s in enumerate(S):
        if s == "S":
            start = (w, h)
        elif s == "G":
            goal = (w, h)
        elif s == "." or s == "#":
            continue
        else:
            tereport[s].append((w, h))

que = deque([(start)])
used_g[start[1]][start[0]] = 0

MOV = [(0, 1), (1, 0), (-1, 0), (0, -1)]
while que:
    here = que.popleft()
    for mov in MOV:
        x, y = (here[0] + mov[0], here[1] + mov[1])
        if x < 0 or W <= x or y < 0 or H <= y:
            continue
        if V[y][x] != "#":
            if used_g[y][x] == 1e9:
                que.append((x, y))
            used_g[y][x] = min(used_g[y][x], used_g[here[1]][here[0]] + 1)

    if V[here[1]][here[0]] in list(string.ascii_lowercase):
        for x, y in tereport[V[here[1]][here[0]]]:
            if used_g[y][x] == 1e9:
                que.append((x, y))
            used_g[y][x] = min(used_g[y][x], used_g[here[1]][here[0]] + 1)
        tereport[V[here[1]][here[0]]] = []

if used_g[goal[1]][goal[0]] == 1e9:
    print(-1)
else:
    print(used_g[goal[1]][goal[0]])