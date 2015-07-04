import sys
import re
import pprint
from random import randint

# function to get random unique word from list
def get_unique_word():
    unique_words = list(set(all_words))

    return unique_words[randint(0, len(unique_words) - 1)]

# funtion to recursively generate likely orders of words
def get_next(index, recursion=0):

    # get the word
    word = all_words[index]

    # create empty dictionary for words that occur after current word
    next_words = {}

    # loop over al the words
    for j, match in enumerate(all_words):

        # if it's an instance of the current word, add the next word to the dict
        # (unless we're at the end of the list)
        if match == word:

            if j >= len(all_words) - 1:
                next_word = get_unique_word()
            else:
                next_word = all_words[j + 1]

            # count the frequency of each next word in the dict
            if next_word in next_words:
                next_words[next_word] += 1
            else:
                next_words.update({next_word: 1})

    # sort the dict and take the 5 highest frequency words
    options = sorted(next_words, key=next_words.get, reverse=True)[:5]

    # pick one
    chosen_next = options[randint(0, len(options) - 1)]
    
    # print it
    print(chosen_next + " "),

    # either recurse or 
    if recursion < 10:
        return get_next(all_words.index(chosen_next), recursion + 1)
    else:
        return


# open file
f = open(sys.argv[1], "r")

# read in text
all_text = f.read()

# remove all punctuation
clean_text = re.sub(r'[^a-zA-Z0-9]'," ", all_text)

lower_text = clean_text.lower()

# split into words
all_words = lower_text.split()

unique_words = list(set(all_words))

index = all_words.index(unique_words[randint(0, len(unique_words) - 1)])

get_next(index)


