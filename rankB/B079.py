names = input().split()
alf = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
nums = [i for i in range(26)]
alf_dict = dict(zip(alf, nums))


def culculate_name(name):
    num_list = []
    for i in name:
        num_list.append(nametonum(i))
    return culc(num_list)


def nametonum(char):
    num = alf_dict[char]
    return num + 1


def culc(num_list) -> int:
    i = 0
    while len(num_list) > 1:
        if i + 1 == len(num_list):
            num_list.pop(i)
            i = 0
            continue
        num1 = num_list[i]
        num2 = num_list[i + 1]
        num = num1 + num2
        if num > 101:
            num -= 101
        num_list[i] = num
        i += 1
    return num_list[0]


pat1 = culculate_name(names[0] + names[1])
pat2 = culculate_name(names[1] + names[0])
if pat1 > pat2:
    print(pat1)
else:
    print(pat2)
