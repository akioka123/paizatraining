nums = list(map(int, input().split()))
turms = nums[0]
unit = nums[1]
num_list = list()
max_num = 0
for i in range(turms):
    num = int(input())
    num = num // unit
    if num > max_num:
        max_num = num
    num_list.append(num)


def makeline(num, max_num):
    strline = "." * max_num
    return strline.replace(".", "*", num)


for index, i in enumerate(num_list):
    ans = str(index + 1) + ":" + makeline(i, max_num)
    print(ans)
