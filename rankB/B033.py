# 入力取得
title_num = int(input())
titles = input().split()
# 列幅
column_width = []
for i in titles:
    column_width.append(len(i))
rows = int(input())
row_list = []
for i in range(rows):
    row = input().split()
    for index, m in enumerate(row):
        if len(m) > column_width[index]:
            column_width[index] = len(m)
    row_list.append(row)
separater = "|"
hyphn = "-"
blank = " "
row_line = separater
for i in range(len(titles)):
    row_line += blank
    row_line += titles[i]
    row_line += blank * (column_width[i] - len(titles[i]))
    row_line += blank + separater
print(row_line)
row_line = separater
for i in range(title_num):
    row_line += hyphn
    row_line += hyphn * column_width[i]
    row_line += hyphn + separater
print(row_line)
for i in range(rows):
    row_line = separater
    for m in range(title_num):
        row_line += blank
        row_line += row_list[i][m]
        row_line += blank * (column_width[m] - len(row_list[i][m]))
        row_line += blank + separater
    print(row_line)
