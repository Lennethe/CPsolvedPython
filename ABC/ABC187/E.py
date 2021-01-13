from sys import stdin

N = int(stdin.readline().rstrip())

edge = [(0, 0)] * (N + 1)
graph = [[] for i in range(N + 1)]

for i in range(N-1):
    A, B = [int(x) for x in stdin.readline().rstrip().split()]
    graph[A].append(B)
    graph[B].append(A)
    edge[i+1] = (A, B)

depth = [-1e9] * (N + 1)
q = [1]
depth[1] = 0

while q:
    here = q.pop()
    for there in graph[here]:
        if depth[here] > depth[there]:
            q.append(there)
            depth[there] = depth[here] - 1


Q = int(stdin.readline().rstrip())

edge_score = [0] * (N + 1)

for i in range(Q):
    T, E, X = [int(x) for x in stdin.readline().rstrip().split()]
    A, B = edge[E]
    if depth[A] > depth[B]:
        if T == 1:
            edge_score[1] += X
            edge_score[B] -= X
        if T == 2:
            edge_score[B] += X
    else:
        if T == 2:
            edge_score[1] += X
            edge_score[A] -= X
        if T == 1:
            edge_score[A] += X

acc_edge_score = [0] * (N + 1)

q = [1]

while q:
    here = q.pop()
    for there in graph[here]:
        if depth[here] > depth[there]:
            q.append(there)
            edge_score[there] += edge_score[here]

for i in range(1, (N + 1)):
    print(edge_score[i])
