import random
from word_listing import words

def define_word():
     """
    Gets word from word_listing 
    and returns it upper case
    """
    word = random.choice(words)
    return word.upper()

def hangman_image(error):
    """
    If/elif to
    Prints image based on error count
    """
    if (error == 0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif (error == 1):
        print("\n+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")
    elif (error == 2):
        print("\n+---+")
        print("O   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif (error == 3):
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif (error == 4):
         print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("   ===")
    elif (error == 5):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif (error == 6):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("    ===")
