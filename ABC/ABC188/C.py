from sys import stdin

n = int(stdin.readline().rstrip())
v = [int(x) for x in stdin.readline().rstrip().split()]
left = max(v[:int(len(v)/2)])
right = max(v[int(len(v)/2):])

if left < right:
    print(v.index(left)+1)
else:
    print(v.index(right)+1)
