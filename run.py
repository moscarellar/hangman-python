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


### Def that will update word and print it
def wordPrintUpdate(lettersGuessed):
    times=0
    rightLetters=0
    for char in word:
        if(char in lettersGuessed):
            print(randomWord[times], end=" ")
            rightLetters+=1
        else:
            print("_", end=" ")
            times+=1
    return rightLetters


def hangman(word):
    complete_word = "_" * len(word)
    lettersGuessed = []
    error = 0
    print("Welcome to Hangman!")
    print(hangman_image(error))