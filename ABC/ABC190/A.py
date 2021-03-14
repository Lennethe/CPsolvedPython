from sys import stdin
A, B, C = [int(x) for x in stdin.readline().rstrip().split()]
if A < B or (A == B and C == 0):
    print("Aoki")
else:
    print("Takahashi")
