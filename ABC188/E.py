from sys import stdin
from collections import defaultdict, deque

dic = defaultdict(list)
money = defaultdict(int)
low_money = defaultdict(int)

N, M = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()]
for i in range(N):
    money[i+1] = A[i]
    low_money[i+1] = 1e13

for i in range(M):
    X, Y = [int(x) for x in stdin.readline().rstrip().split()]
    dic[X].append(Y)

dq = deque()

is_used = [False] * (N+1)

sort_town = sorted(money.items(), key=lambda x:x[1])

for i, mny in sort_town:
    dq.append(i)

    while len(dq) > 0:
        here = dq.popleft()
        if is_used[here]:
            continue
        is_used[here] = True
        for there in dic[here]:
            low_money[there] = min(low_money[here], low_money[there], money[here])
            dq.append(there)


ans = -1e13
for k in money.keys():
    ans = max(ans, money[k] - low_money[k])


print(ans)
