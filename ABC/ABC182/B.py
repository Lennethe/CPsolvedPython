from sys import stdin
from collections import defaultdict

def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

_ = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()]

dic = defaultdict(int)
for a in A:
    for k in make_divisors(a):
        if k == 1:
            continue
        dic[k] += 1

for k, v in dic.items():
    if v == max(dic.values()):
        print(k)
        exit()
