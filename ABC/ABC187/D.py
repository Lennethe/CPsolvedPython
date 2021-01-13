from sys import stdin

n = int(stdin.readline().rstrip())
aoki = 0
takahashi = 0
vote = []
for i in range(n):
    x, y = [int(x) for x in stdin.readline().rstrip().split()]
    vote.append(x+y+x)
    aoki += x
vote = sorted(vote, reverse=True)

for i, v in enumerate(vote):
    takahashi += v
    if aoki < takahashi:
        print(i+1)
        break
