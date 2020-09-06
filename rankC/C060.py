input_list = list(map(int, input().split()))
word_num = input_list[0]
page_num = input_list[1]
target_page = input_list[2]
alp = [
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
alp_dict = dict(zip(alp, nums))


def compair_word(word1, word2):
    global alp_dict
    for i in range(len(word1)):
        if alp_dict[word1[i]] > alp_dict[word2[i]]:
            return 1
        if alp_dict[word1[i]] == alp_dict[word2[i]]:
            return 0
        if alp_dict[word1[i]] < alp_dict[word2[i]]:
            return -1


word_list = []
for i in range(word_num):
    word = input()
    if word_list == []:
        word_list.append(word)
    else:
        word_list.append("")
        for i in word_list:
            compair_word(word, i)
