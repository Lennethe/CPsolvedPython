from sys import stdin

a, b = [int(x) for x in stdin.readline().rstrip().split()]
c, d = [int(x) for x in stdin.readline().rstrip().split()]

def judge(a, b, c, d):
    return a + b == c + d or a - b == c - d or abs(a-c) + abs(b-d) <= 3


if a == c and b == d:
    print(0)
    exit()

if judge(a, b, c, d):
    print(1)
    exit()

for i in range(-3, 4):
    for j in range(-3, 4):
        if abs(i) + abs(j) <= 3:
            c1 = c + i
            d1 = d + j
            if judge(a, b, c1, d1):
                print(2)
                exit()

if (a+b)%2 == (c+d)%2:
    print(2)
    exit()

print(3)

