import random
from word_listing import words

def define_word():
    word = random.choice(words)
    return word.upper()

word = define_word()



def hangman_image(error):
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
            print(word[times], end=" ")
            rightLetters+=1
        else:
            print("_", end=" ")
            times+=1
    return rightLetters


def hangman(word):
    complete_word = "_" * len(word)
    letters_guessed = []
    error = 0
    current_letters_right = 0
    discovered = False
    print("Welcome to Hangman!")
    print(hangman_image(error))
    print(complete_word)
    print("\n")
    while(error != 6 and not discovered):
        interaction = input("Guess a letter: ").upper()
        if len(interaction) == 1 and interaction.isalpha():
            if interaction in letters_guessed:
                print("You already guessed the letter", interaction)
            elif interaction not in word:
                print(interaction, "is not in the word.")
                error += 1
                letters_guessed.append(interaction)
                hangman_image(error)
                wordPrintUpdate(letters_guessed)
            else:
                print("Well done,", interaction, "is in the word!")
                letters_guessed.append(interaction)
                
                indexed_word = list(complete_word)
                indexes = [i for i, letter in enumerate(word) if letter == interaction]
                for index in indexes:
                    indexed_word [index] = guess
                complete_word = "".join(indexed_word)


def game():
    hangman(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        hangman(word)

game()
