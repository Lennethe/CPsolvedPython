from sys import stdin


def solve(v, d):
    a = v // d
    b = v % d
    if b == 7:
        return False
    elif a == 0:
        return True
    else:
        return solve(a, d)


N = int(stdin.readline().rstrip())

ans = 0
for i in range(1, N + 1):
    if solve(i, 10) and solve(i, 8):
        ans += 1

print(ans)