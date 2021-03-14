from sys import stdin


def step1(xy):
    return (xy[1], -xy[0])


def step2(xy):
    return (-xy[1], xy[0])


def step3(xy, p):
    return (2*p-xy[0], xy[1])


def step4(xy, p):
    return (xy[0], 2*p-xy[1])


origin = [0, 0]
x_one = [1, 0]
y_one = [0, 1]

N = int(stdin.readline().rstrip())
XY = []
for i in range(N):
    XY.append([int(x) for x in stdin.readline().rstrip().split()])

M = int(stdin.readline().rstrip())
OP = [[origin, x_one, y_one]]


for i in range(M):
    AB = [int(x) for x in stdin.readline().rstrip().split()]
    if AB[0] == 1:
        OP.append([step1(OP[-1][0]), step1(OP[-1][1]), step1(OP[-1][2])])
    if AB[0] == 2:
        OP.append([step2(OP[-1][0]), step2(OP[-1][1]), step2(OP[-1][2])])
    if AB[0] == 3:
        OP.append([step3(OP[-1][0], AB[1]), step3(OP[-1][1], AB[1]), step3(OP[-1][2], AB[1])])
    if AB[0] == 4:
        OP.append([step4(OP[-1][0], AB[1]), step4(OP[-1][1], AB[1]), step4(OP[-1][2], AB[1])])

Q = int(stdin.readline().rstrip())

for i in range(Q):
    A, B = [int(x) for x in stdin.readline().rstrip().split()]
    op = OP[A]
    XYi = XY[B-1]
    x_vec = [(op[1][0]-op[0][0]) * XYi[0], (op[1][1]-op[0][1]) * XYi[0]]
    y_vec = [(op[2][0]-op[0][0]) * XYi[1], (op[2][1]-op[0][1]) * XYi[1]]
    print(op[0][0] + x_vec[0] + y_vec[0], op[0][1] + x_vec[1] + y_vec[1])
