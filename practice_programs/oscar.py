"""
We define a name chain like so:

A name is a composite type containing first_name and last_name strings. For example, in pseudocode we can represent it in this way:
           class Name {

              string first_name

              string last_name

           }

Names A and B form a name chain if A.last_name == B.first_name.
Names A, B, and C form a name chain if A.last_name == B.first_name and B.last_name == C.first_name, and so on and so forth.
Given a list of names, return the length of the longest name chain that can be formed using names in the list.

You may assume any convenient representation for an input name, tuples or objects are both fine. You may, of course, use intermediate data structures to store names if you find it helpful.

Assume that the input list will not contain duplicate names, ex: [('bob', 'ross'), ('bob', 'ross')]

Assume that the input list will not contain cyclical name chains, ex: [('bob', 'ross'), ('ross', 'bob')]

def int longest_name_chain(List<Name> names) {

    ...

}

SOME SAMPLES

[('bob', 'ross'), ('ross', 'miller'), ('brown', 'cow'), ('ross', 'brown')] => 3

[] => 0

[('bobby', 'bob')] => 1

[('anna', 'bob'), ('bob', 'casey'), ('casey', 'dean')] => 3
"""


# import requests
# import mysql.connector
# import pandas as pd
def longest_name_chain(names: dict) -> int:
    """
    The method takes names and provides the longest chan length
    """
    max_chain_length = 0
    if len(names) == 0: 
        max_chain_length = 0
    elif len(names) == 1:
        max_chain_length = 1 
    
    for key, val in names.items(): # n O(n^2)
        chain = list()
        starting_name = key + " " + val
        chain.append(starting_name) # boss ross
        names_rem = {k: v for k, v in names.items() if k != key}
        counter = len(names_rem)
        memo = {}
        if starting_name not in memo:
            while len(names_rem) >= 1 and counter >= 1: # n -1

                last_name = chain[len(chain) - 1].split(" ")[1]
                if last_name in names_rem:
                    chain.append(last_name + " " + names_rem[last_name])
                    names_rem = {k: v for k, v in names_rem.items() if k != last_name}
                counter -= 1
            max_chain_length = max(max_chain_length, len(chain))
            memo[last_name] = max_chain_length
    return max_chain_length
            
    
#input_names = {'bob': 'ross', 'ross': 'miller' ,'brown': 'cow', 'ross': 'brown'}

# bob ross - ross miller =>2, bob ross - ross brown brown  cow
# ross miller

#input_names = {'anna': 'bob', 'bob': 'casey', 'casey': 'dean'} 
#input_names = {}
# input_names = {'anna': 'bob'}
input_names = {'casey': 'dean', 'bob': 'casey', 'anna': 'bob'}  # => 3
print(longest_name_chain(input_names))

