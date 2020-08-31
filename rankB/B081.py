"""
    隣にあるかどうか　⇒　-2
"""
input_list = list(map(int, input().split()))
height = input_list[0]
width = input_list[1]
fb = []
for i in range(height):
    fb += input().split()
i = 0
roap_count = 0
while i < len(fb):
    for index, flower in enumerate(fb[i]):
        roap = 0
        if flower == "#":
            roap = 4
            # 上下左右を検査
            # 上下
            if i - 1 >= 0:
                if fb[i - 1][index] == "#":
                    roap -= 1
            if i < height - 1:
                if fb[i + 1][index] == "#":
                    roap -= 1
            # 左右
            if index - 1 >= 0:
                if fb[i][index - 1] == "#":
                    roap -= 1
            if index < width - 1:
                if fb[i][index + 1] == "#":
                    roap -= 1
        roap_count += roap
    i += 1
print(roap_count)
