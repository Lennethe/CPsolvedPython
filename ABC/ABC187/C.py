from sys import stdin

n = int(stdin.readline().rstrip())
v = set([stdin.readline().rstrip() for _ in range(n)])

for s in v:
    if "!" + s in v:
        print(s)
        break
else:
    print("satisfiable")
