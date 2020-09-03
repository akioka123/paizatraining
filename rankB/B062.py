time = int(input())
input_list = list(map(int, input().split()))
height = input_list[0]
width = input_list[1]
room = list()
for i in range(height):
    room.append(input())
direction = "r"
cells = [0, 0]
is_wall = False
clean = 0
min_height = 0
max_height = height - 1
min_width = 0
max_width = width - 1


# direction is "u", "d", "r", "l"
def turn(cells):
    global direction, min_height, max_height, min_width, max_width
    if cells[1] == max_height and direction == "d":
        max_width -= 1
        direction = "l"
    if cells[1] == min_height and direction == "u":
        min_width += 1
        direction = "r"
    if cells[0] == max_width and direction == "r":
        min_height += 1
        direction = "d"
    if cells[0] == min_width and direction == "l":
        max_height -= 1
        direction = "u"


def move(direction, cells):
    if direction == "u":
        cells[1] -= 1
    if direction == "d":
        cells[1] += 1
    if direction == "r":
        cells[0] += 1
    if direction == "l":
        cells[0] -= 1
    return cells


for i in range(time):
    if room[cells[1]][cells[0]] == "#":
        clean += 1
    turn(cells)
    cells = move(direction, cells)
print(clean)
