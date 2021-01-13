from sys import stdin

n = int(stdin.readline().rstrip())
a = [int(x) for x in stdin.readline().rstrip().split()]
b = [int(x) for x in stdin.readline().rstrip().split()]

ans = 0
for i in range(n):
    ans += a[i] * b[i]

if ans == 0:
    print("Yes")
else:
    print("No")