import random
from word_listing import words

def generate_new_word():
    word = random.choice(words)
    return word.upper()

word = generate_new_word()


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


def hangman(word):
    complete_word = "_" * len(word)
    letters_guessed = []
    words_guessed = []
    error = 0
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
            else:
                print("Well done,", interaction, "is in the word!")
                letters_guessed.append(interaction)
                indexed_word = list(complete_word)
                indexes = [i for i, letter in enumerate(word) if letter == interaction]
                for index in indexes:
                    indexed_word [index] = interaction
                complete_word = "".join(indexed_word)
                if "_" not in complete_word:
                    discovered = True
        elif len(interaction) == len(word) and interaction.isalpha():
            if interaction in words_guessed:
                print("You have guessed his word already, ", word)
            elif interaction != word:
                print(ineraction, " is not the word")
                error += 1
                words_guessed.append(interaction)
            else:
                interaction = True
                complete_word = word
        else:
            print("Wrong guess")
        print(complete_word)
        print("\n")
    if discovered:
        print("Well done")
    else:
        print("Game over. Word was " + word + ".")
        





def game():
    hangman(word)
    

game()
