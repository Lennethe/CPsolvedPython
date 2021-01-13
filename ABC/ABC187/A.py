from sys import stdin


def solve(string):
    ans = 0
    for s in string:
        ans += int(s)
    return ans


a, b = [str(x) for x in stdin.readline().rstrip().split()]

print(max(solve(a), solve(b)))
