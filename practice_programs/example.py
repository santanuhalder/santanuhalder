def longest_name_chain(names: dict) -> int:
    max_chain_length = 0
    name_set = set(names.keys())
    memo = {}

    for key, val in names.items():
        if val.split()[-1] in name_set:
            chain_length = 1
            current_key = val.split()[-1]
            while current_key in name_set:
                if current_key in memo:
                    chain_length += memo[current_key]
                    break
                current_key = names[current_key].split()[-1]
                chain_length += 1
            max_chain_length = max(max_chain_length, chain_length)
            # Memoize the chain length for the current key
            memo[key] = chain_length - 1
    return max_chain_length


input_names = {'bob': 'ross', 'ross': 'miller','brown': 'cow'}

# input_names = {'casey': 'dean', 'bob': 'casey', 'anna': 'bob'}  # => 3
print(longest_name_chain(input_names))