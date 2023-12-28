def longest_name_chain(names):
    max_length = 0
    for key, value in names.items():
        name_chain = []
        name_chain.append(key + " " + value)
        names_ = {k: v for k, v in names.items() if k != key}
        counter = len(names_)
        while len(names_) >=1 and counter >=1:
            last_name = name_chain[len(name_chain) - 1].split(" ")[1]
            if last_name in names_:
                name_chain.append(last_name + " " + names_[last_name])
                names_ = {k: v for k, v in names_.items() if k != last_name}
            counter -= 1
        max_length = max(max_length, len(name_chain))
    return max_length

def count_keys(input_dict):
    key_count = 0
    for key in input_dict.keys():
        key_count += 1
    return key_count

name_set = {'alice': 'bob',
            'bob1': 'ross',
            'alex': 'johnson',
            'ross': 'alex'}
# result = longest_name_chain(name_set)
# print("Longest Name Chain Length:", result)



print(longest_name_chain(name_set))
