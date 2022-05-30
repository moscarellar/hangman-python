import random
from word_listing import words

def define_word():
    word = random.choice(words)
    return word.upper()

