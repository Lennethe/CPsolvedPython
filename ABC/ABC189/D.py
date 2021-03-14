from sys import stdin

N = int(stdin.readline().rstrip())
z, o = 1, 1
for i in range(N):
    string = stdin.readline().rstrip()
    if string == "AND":
        z = (z+o)*2 - o
    if string == "OR":
        o = (z+o)*2 - z

print(o)
