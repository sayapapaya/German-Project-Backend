import cPickle as pickle

"""
This file preprocessed 'german_english.txt' to create a Python dictionary
mapping German words to English words.

The dictionary is dumped to a pickle file so that it can be efficiently
loaded by the API.
"""
german_english_dict = {}

with open("german_english.txt") as file:
    all_lines = file.readlines()
    
    for line in all_lines:
        line_parts = line.split(';')
        for part in line_parts:
            key = None
            val = None

            tabsplit = part.split('\t')
            if len(tabsplit) == 2:
                key = tabsplit[0].strip(' ')
                val = tabsplit[1].strip(' ')

            if (key and val):
                german_english_dict[key] = val
                break


output_file = open("dictionary.p", "wb")
pickle.dump(german_english_dict, output_file)
output_file.close()


    
        
