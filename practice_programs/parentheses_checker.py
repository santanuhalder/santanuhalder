input_str = "{[[{}]]}"
parenthesis_dict = {'{': '}', '(': ')', '[': ']'}
parenthesis_list = list()
is_valid = True

for i in range(len(input_str)):
    current_char = input_str[i]
    if parenthesis_dict.get(current_char) != None:
        parenthesis_list.append(current_char)
    else:
        if len(parenthesis_list) == 0:
            parenthesis_list.append(current_char)
        else:
            last_list_item = parenthesis_list[len(parenthesis_list) - 1]
            if parenthesis_dict[last_list_item] == current_char:
                parenthesis_list.pop(len(parenthesis_list) - 1)


print(parenthesis_list)
print(not parenthesis_list)







