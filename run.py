import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('guestbook_hangman')

gb = SHEET.worksheet('guestbookworksheet')
data = gb.get_all_values()

print(data)

import random
from word_listing import words

def generate_new_word():
    word = random.choice(words)
    return word.upper()


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
        else:
            print("Wrong guess, please type only one letter")
        print(complete_word)
        print("\n")
    if discovered:
        print("Well done")
    else:
        print("Game over. Word was " + word + ".")


def game():
    word = generate_new_word()
    hangman(word)
    while input("Play Again? ( yes / no ) ") == "yes":
        word = generate_new_word()
        hangman(word)

game()
