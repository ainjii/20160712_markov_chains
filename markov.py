from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()

    return contents


def make_chains(text_string):
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

    
    #get keys for chains dictionary
    for i in range(len(words)-2):

        chains_key = tuple(words[i:i+2])
        #chains = (words[i], words[i+1])

        chains_value = words[i+2]

        #print chains_key
        #print chains_value
    
        chains[chains_key] = chains.get(chains_key, [])
        # don't assign this to a value because .append returns none
        chains[chains_key].append(chains_value)

        #print chains
    
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    key = choice(chains.keys())

    while chains.get(key, False):
        next_word = choice(chains[key])
        text += "{} ".format(next_word)
        key = (key[1], next_word)

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
# print chains
# Produce random text
random_text = make_text(chains)

print random_text
