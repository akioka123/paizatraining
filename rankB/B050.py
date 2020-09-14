import re

words = int(input())
keyword = input()


def is_match(word):
    global keyword
    if keyword in word:
        return True
    for i in range(len(keyword)):
        word_head = keyword[:i]
        word_tail = keyword[i:]
        reword = re.escape(word_head) + r"." + re.escape(word_tail)
        result = re.search(reword, word)
        if result:
            return True
    return False


for i in range(words):
    word = input()
    if is_match(word):
        print("valid")
    else:
        print("invalid")
