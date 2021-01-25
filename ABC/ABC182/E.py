from sys import stdin

H, W, N, M = [int(x) for x in stdin.readline().rstrip().split()]

Akari = []
for i in range(N):
    Akari.append([int(x) for x in stdin.readline().rstrip().split()])

block = [([0] * (W+1)) for _ in range(H+1)]

for i in range(M):
    tate, yoko = [int(x) for x in stdin.readline().rstrip().split()]
    block[tate-1][yoko-1] = 1

field_tate = [([0] * (W)) for _ in range(H)]
field_yoko = [([0] * (W)) for _ in range(H)]

for i in range(N):
    tate, yoko = Akari[i]
    tate -= 1
    yoko -= 1
    if field_tate[tate][yoko] == 0:
        mv = 0
        while tate + mv < H and block[tate + mv][yoko] == 0:
            field_tate[tate+mv][yoko] = 1
            mv += 1
        mv = 0
        while tate - mv >= 0 and block[tate - mv][yoko] == 0:
            field_tate[tate-mv][yoko] = 1
            mv += 1
    if field_yoko[tate][yoko] == 0:
        mv = 0
        while yoko + mv < W and block[tate][yoko + mv] == 0:
            field_yoko[tate][yoko + mv] = 1
            mv += 1
        mv = 0
        while yoko - mv >= 0 and block[tate][yoko - mv] == 0:
            field_yoko[tate][yoko - mv] = 1
            mv += 1

ans = 0
for i in range(H):
    for j in range(W):
        if field_tate[i][j] + field_yoko[i][j] > 0:
            ans += 1

print(ans)
