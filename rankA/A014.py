input_list = list(map(int, input().split()))
height = input_list[0]
width = input_list[1]
pair_num = input_list[2]
cards = []
cards.append("." * (width + 2))
for i in range(height):
    card_line = input()
    card_line = card_line.replace(" ", "")
    card_line += "."
    card_line = "." + card_line
    cards.append(card_line)
cards.append("." * (width + 2))
blank_dire = ""


# 同じ文字か判定
def is_match_char(cells1, cells2):
    global cards
    is_match = False
    card1 = cards[cells1[0]][cells1[1]]
    card2 = cards[cells2[0]][cells2[1]]
    if card1 == card2:
        is_match = True
    return is_match


def is_edge(point):
    global height, width
    if point == 1 or point == height or point == width:
        return True
    return False


def have_blank(cell):
    global cards, blank_dire
    if cards[cell[0] + 1][cell[1]] == ".":
        blank_dire = "d"
        return True
    if cards[cell[0] - 1][cell[1]] == ".":
        blank_dire = "u"
        return True
    if cards[cell[0]][cell[1] + 1] == ".":
        blank_dire = "r"
        return True
    if cards[cell[0]][cell[1] - 1] == ".":
        blank_dire = "l"
        return True
    return False


def check_direction(scell, ecell, cell_diff):
    global cards
    is_finish = False
    if cell_diff[0] < 0 and cell_diff[1] < 0:
        search_dire = ["r", "d"]
    if cell_diff[0] > 0 and cell_diff[1] > 0:
        search_dire = ["l", "u"]
    if cell_diff[0] > 0 and cell_diff[1] < 0:
        search_dire = ["r", "u"]
    if cell_diff[0] < 0 and cell_diff[1] > 0:
        search_dire = ["l", "d"]
    while not is_finish:
        if "r" in search_dire:
            next_cell = cards[scell[0]][scell[1] + 1]
            if next_cell == ".":
                continue


# 二角で可能か判定
def is_take_twice(cells1, cells2):
    global blank_dire
    # 隣同士、同列は確実に可能　事前に省く
    if is_edge(cells1[0]):
        if cells1[0] == cells2[0]:
            return True
    if is_edge(cells1[1]):
        if cells1[1] == cells2[1]:
            return True
    if cells1[0] == cells2[0]:
        if abs(cells1[1] - cells2[1]) == 1:
            return True
    if cells1[1] == cells2[1]:
        if abs(cells1[0] - cells2[0]) == 1:
            return True
    # 四方向とも空いていない
    if not have_blank(cells1) and not have_blank(cells2):
        return False
    cells_diff = (cells1[0] - cells2[0], cells1[1] - cells2[1])
    # -,- rd ++ lu +- ru -+ ld
    # 方向に空白があるかを検査
    if cells_diff[0] == -1 and cells_diff[1] == -1 and blank_dire in ("r", "d"):
        return True
    if cells_diff[0] == 1 and cells_diff[1] == 1 and blank_dire in ("l", "u"):
        return True
    if cells_diff[0] == 1 and cells_diff[1] == -1 and blank_dire in ("r", "u"):
        return True
    if cells_diff[0] == -1 and cells_diff[1] == 1 and blank_dire in ("l", "d"):
        return True


ans_list = []
for i in range(pair_num):
    input_list = list(map(int, input().split()))
    cells1 = (input_list[0], input_list[1])
    cells2 = (input_list[2], input_list[3])
    if is_match_char(cells1, cells2):
        if is_take_twice(cells1, cells2):
            ans_list.append("yes")
            continue
    ans_list.append("no")

for i in ans_list:
    print(i)
