input_list = list(map(int, input().split()))
square = input_list[0]
call_time = input_list[1]
bingo_card = []
for _ in range(square):
    bingo_card += input().split()
for _ in range(call_time - 1):
    call_num = input()
    if call_num in bingo_card:
        bingo_card[bingo_card.index(call_num)] = ""


def is_blank(target):
    if target == "":
        return True
    return False


""" 
既出ビンゴ及びリーチチェック
空いていないマスの数とマスの番号を記録
"""
# 縦ビンゴ
each_reach = []
for i in range(square):
    not_blank_num = 0
    card_list = []
    for m in range(square):
        card_num = bingo_card[i + m * square]
        if not is_blank(card_num):
            card_list.append(card_num)
            not_blank_num += 1
    result = [not_blank_num, card_list]
    each_reach.append(result)
# 横ビンゴ
for i in range(square):
    not_blank_num = 0
    card_list = []
    for m in range(square):
        card_num = bingo_card[i * square + m]
        if not is_blank(card_num):
            card_list.append(card_num)
            not_blank_num += 1
    result = [not_blank_num, card_list]
    each_reach.append(result)
# 対角線チェック
not_blank_num = 0
card_list = []
for m in range(square):
    card_num = bingo_card[m * (square + 1)]
    if not is_blank(card_num):
        card_list.append(card_num)
        not_blank_num += 1
result = [not_blank_num, card_list]
each_reach.append(result)
not_blank_num = 0
card_list = []
for m in range(1, square + 1):
    card_num = bingo_card[m * (square - 1)]
    if not is_blank(card_num):
        card_list.append(card_num)
        not_blank_num += 1
result = [not_blank_num, card_list]
each_reach.append(result)
# ビンゴ計測　bingo_paturn ビンゴになる番号:ビンゴ数
bingo = 0
bingo_paturn = {}
for i in each_reach:
    if i[0] == 0:
        bingo += 1
    if i[0] == 1:
        if i[1][0] in bingo_paturn:
            bingo_paturn[i[1][0]] += 1
        else:
            bingo_paturn[i[1][0]] = 1
print(bingo + max(bingo_paturn.values()))
