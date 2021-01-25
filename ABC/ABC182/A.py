from sys import stdin

A, B = [int(x) for x in stdin.readline().rstrip().split()]
print(2*A+100 - B)