def prefix(words):
    upper_word =[x.upper() for x in words]
    pre_fix= ""
    list1 = list()

    for i in range(len(upper_word)):
        for j in range(len(upper_word[i])):
            print(upper_word[i][j])


    return pre_fix

word_list = ["Floeer", "Flood", "fl"]
print(prefix(word_list))


