input_list = list(map(int, input().split()))
piece_num = input_list[0]
pazzle_size = input_list[1]
piece_size = input_list[2]
n = piece_size
pazzle = []
num = 0
for i in range(pazzle_size):
    string = input()
    pazzle += [string[i: i + n] for i in range(0, len(string), n)]
piece_list = []
arg = piece_num
for i in range(piece_num):
    piece = []
    for i in range(piece_size):
        piece.append(input())
    piece_list.append(piece)
for _ in range(4):
    list_num = 0
    plus = 0
    for index, i in enumerate(piece_list):
        m = 0
        if pazzle[list_num + plus] == i[m]:
            is_match = True
            while is_match:
                m += 1
                l = list_num + plus  + pazzle_size // piece_size
                if pazzle[l] != i[m]:
                    is_match = False
                if l == (pazzle_size // piece_size) ** 2:
                    piece_list.pop(index)
                    is_match = False
        plus += 1
        if plus == pazzle_size // piece_size - 1:
            plus = 0
            list_num += pazzle_size
print(piece_list)


