from sys import stdin

a = [int(x) for x in stdin.readline().rstrip().split()]
if max(a) - min(a) < 3:
    print("Yes")
else:
    print("No")
