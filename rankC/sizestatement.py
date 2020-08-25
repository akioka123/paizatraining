input_list = list(map(int, input().split()))
height = input_list[0]
width = input_list[1]
change_width = input_list[2]
statement = ""
for i in range(height):
    statement += input()
length = 0
statement_list = []
loop = (width * height) // change_width
loop_mod = (width * height) % change_width
if loop_mod > 0:
    loop += 1
for i in range(loop):
    statement_list.append(statement[length: length + change_width])
    length += change_width
for i in statement_list:
    print(i)