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
    letters_guessed = []
    error = 0
    discovered = False
    print("Welcome to Hangman!")
    print(hangman_image(error))
    print(complete_word)
    print("\n")
    while(error != 6 and not discovered):
        interaction = input("Guess a letter").upper()
        if len(interaction) == 1 and human.isalpha():
            if interaction in letters_guessed:
                print("You already guessed the letter", interaction)
            elif interaction not in word:
                print(interaction, "is not in the word.")
                error += 1
                letters_guessed.append(interaction)
            else:
                print("Well done,", interaction, "is in the word!")
               letters_guessed.append(interaction)
               wordPrintUpdate(letters_guessed)

