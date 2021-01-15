from sys import stdin


a, b = [int(x) for x in stdin.readline().rstrip().split()]
c, d = [int(x) for x in stdin.readline().rstrip().split()]
print(a*d-b*c)
