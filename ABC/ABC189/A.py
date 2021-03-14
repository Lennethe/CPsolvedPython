from sys import stdin


string = stdin.readline().rstrip()
if string[0] == string[1] and string[1] == string[2]:
    print("Won")
else:
    print("Lost")
