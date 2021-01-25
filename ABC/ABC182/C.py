from sys import stdin

string = stdin.readline().rstrip()

zero = 0
one = 0
two = 0
rest = 0

for s in string:
    if int(s) % 3 == 0:
        zero += 1
    if int(s) % 3 == 1:
        one += 1
    if int(s) % 3 == 2:
        two += 1
    rest = (rest + int(s) % 3) % 3


if rest == 0:
    print(0)
elif rest == 1:
    if one > 0 and (zero + one + two) > 1:
        print(1)
    elif two > 1 and (zero + one + two) > 2:
        print(2)
    else:
        print(-1)
else:
    if two > 0 and (zero + one + two) > 1:
        print(1)
    elif one > 1 and (zero + one + two) > 2:
        print(2)
    else:
        print(-1)
