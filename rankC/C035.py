member = int(input())
pass_member = 0
for i in range(member):
    input_list = input().split()
    which = input_list[0]
    eng = int(input_list[1])
    math = int(input_list[2])
    sci = int(input_list[3])
    jap = int(input_list[4])
    his = int(input_list[5])
    all_point = eng + math + sci + jap + his
    is_pass = False
    if which == "l":
        if (jap + his) >= 160 and all_point >= 350:
            is_pass = True
    elif which == "s":
        if (math + sci) >= 160 and all_point >= 350:
            is_pass = True
    if is_pass:
        pass_member += 1
print(pass_member)
