from sys import stdin

N, M, T = [int(x) for x in stdin.readline().rstrip().split()]
e = N
t = 0
for i in range(M):
    A, B = [int(x) for x in stdin.readline().rstrip().split()]
    e -= A - t
    if e <= 0:
        print("No")
        break
    e = min(e + B - A, N)
    t = B
else:
    if T - t >= e:
        print("No")
    else:
        print("Yes")
