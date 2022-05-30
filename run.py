import random
from word_listing import words

def define_word():
     """
    Gets word from word_listing 
    and returns it upper case
    """
    word = random.choice(words)
    return word.upper()



