from sys import stdin
from collections import defaultdict

n, def_c = [int(x) for x in stdin.readline().rstrip().split()]
dic = defaultdict(int)

for i in range(n):
    a, b, c = [int(x) for x in stdin.readline().rstrip().split()]
    dic[a] += c
    dic[b+1] -= c

now_cost = 0
ans = 0
day = 0
for k, v in sorted(dic.items()):
    ans += (k - day) * min(now_cost, def_c)
    now_cost += v
    day = k

print(ans)

