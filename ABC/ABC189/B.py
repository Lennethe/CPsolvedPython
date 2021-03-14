from sys import stdin


N, M = [int(x) for x in stdin.readline().rstrip().split()]

sm = 0
for i in range(N):
    V, P = [int(x) for x in stdin.readline().rstrip().split()]
    sm += V * P
    if M*100 < sm:
        print(i+1)
        exit()
print(-1)
