from sys import stdin

sx, sy, gx, gy = [int(x) for x in stdin.readline().rstrip().split()]
gy = -gy

a = (gy - sy)/(gx - sx)
b = sy - a * sx

print(-b/a)
