from random import choice
from sys import argv


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()

    return contents


def make_chains(text_string, n):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    words = text_string.split()

    
    # get keys for chains dictionary
    for i in range(len(words)-n):

        chains_key = tuple(words[i:i+n])
        # chains = (words[i], words[i+1])

        chains_value = words[i+n]

        # print chains_key
        # print chains_value
    
        chains[chains_key] = chains.get(chains_key, [])
        # don't assign this to a value because .append returns none
        chains[chains_key].append(chains_value)

        # print chains
    
    return chains


def make_text(chains, n):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    
    cap_keys = [key for key in chains.keys() if key[0] == key[0].capitalize()]
    key = choice(cap_keys)

    while chains.get(key, False):
        next_word = choice(chains[key])
        text += "{} ".format(next_word)

        # start range at 1 because don't need first element in key (already used)
        key_list = [key[i] for i in range(1, len(key))]
        key_list.append(next_word)

        key = tuple(key_list)
        # print key will print out the tuple of 3 elements

    return text


input_path = argv[1]
n = int(argv[2])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n)

# Produce random text
random_text = make_text(chains, n)

print random_text
