input_list = list(map(int, input().split()))
member = input_list[0]
rank = input_list[1]
eng = {}
math = {}
jap = {}
for i in range(member):
    input_list = list(map(int, input().split()))
    eng[i] = input_list[0]
    jap[i] = input_list[1]
    math[i] = input_list[2]
sort_eng = sorted(eng.items(), key=lambda x: x[1])
sort_jap = sorted(jap.items(), key=lambda x: x[1])
sort_math = sorted(math.items(), key=lambda x: x[1])
bad_list = [0] * member
low_num = 100
rank_num = 0
for i in sort_eng:
    if low_num > i[1]:
        low_num = i[1]
        bad_list[i[0]] += 1
        rank_num += 1
    elif low_num == i[1]:
        bad_list[i[0]] += 1
        rank_num += 1
    else:
        if rank_num >= rank:
            break
        else:
            bad_list[i[0]] += 1
            rank_num += 1
            continue
low_num = 100
rank_num = 0
for i in sort_jap:
    # 初期値
    if low_num > i[1]:
        low_num = i[1]
        bad_list[i[0]] += 1
        rank_num += 1
    # 同値
    elif low_num == i[1]:
        bad_list[i[0]] += 1
        rank_num += 1
    else:
        if rank_num >= rank:
            break
        else:
            bad_list[i[0]] += 1
            rank_num += 1
            continue
low_num = 100
rank_num = 0
for i in sort_math:
    if low_num > i[1]:
        low_num = i[1]
        bad_list[i[0]] += 1
        rank_num += 1
    elif low_num == i[1]:
        bad_list[i[0]] += 1
        rank_num += 1
    else:
        if rank_num >= rank:
            break
        else:
            bad_list[i[0]] += 1
            rank_num += 1
            continue
for i in bad_list:
    print(i)


