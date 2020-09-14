input_list = list(map(int, input().split()))
start_x = input_list[0]
start_y = input_list[1]
input_list = list(map(int, input().split()))
move_point = [input_list[0], input_list[1], input_list[2], input_list[3]]
order_times = int(input())
# u, r, d, l ロボットのむいている方向
robot = ["u", [start_x, start_y]]


def turn(direction, now_direction):
    global robot
    if direction == "R":
        if robot[0] == "u":
            return "r"
        if robot[0] == "r":
            return "d"
        if robot[0] == "d":
            return "l"
        if robot[0] == "l":
            return "u"
    if direction == "B":
        if robot[0] == "u":
            return "d"
        if robot[0] == "r":
            return "l"
        if robot[0] == "d":
            return "u"
        if robot[0] == "l":
            return "r"
    if direction == "L":
        if robot[0] == "u":
            return "l"
        if robot[0] == "r":
            return "u"
        if robot[0] == "d":
            return "r"
        if robot[0] == "l":
            return "d"


def move(direction):
    global robot, move_point
    if direction == "F":
        if robot[0] == "u":
            robot[1][1] += move_point[0]
        if robot[0] == "r":
            robot[1][0] += move_point[0]
        if robot[0] == "d":
            robot[1][1] -= move_point[0]
        if robot[0] == "l":
            robot[1][0] -= move_point[0]
    if direction == "R":
        if robot[0] == "u":
            robot[1][0] += move_point[1]
        if robot[0] == "r":
            robot[1][1] -= move_point[1]
        if robot[0] == "d":
            robot[1][0] -= move_point[1]
        if robot[0] == "l":
            robot[1][1] += move_point[1]
    if direction == "B":
        if robot[0] == "u":
            robot[1][1] -= move_point[2]
        if robot[0] == "r":
            robot[1][0] -= move_point[2]
        if robot[0] == "d":
            robot[1][1] += move_point[2]
        if robot[0] == "l":
            robot[1][0] += move_point[2]
    if direction == "L":
        if robot[0] == "u":
            robot[1][0] -= move_point[3]
        if robot[0] == "r":
            robot[1][1] += move_point[3]
        if robot[0] == "d":
            robot[1][0] += move_point[3]
        if robot[0] == "l":
            robot[1][1] -= move_point[3]


for i in range(order_times):
    order_list = input().split()
    if order_list[0] == "m":
        move(order_list[1])
    if order_list[0] == "t":
        robot[0] = turn(order_list[1], robot[0])

ans_position = ""
for i in robot[1]:
    ans_position += str(i)
    ans_position += " "

print(ans_position.rstrip())
