input_list = input().split()
first = input_list[0]
operand = input_list[1]
second = input_list[2]
equal = input_list[3]
answer = input_list[4]
ans = 0
if operand == "+":
    if first == "x":
        ans = int(answer) - int(second)
    elif second == "x":
        ans = int(answer) - int(first)
    elif answer == "x":
        ans = int(first) + int(second)
if operand == "-":
    if first == "x":
        ans = int(answer) + int(second)
    elif second == "x":
        ans = int(first) - int(answer)
    elif answer == "x":
        ans = int(first) - int(second)
print(ans)
