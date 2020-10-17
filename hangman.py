# importing required packages
from english_words import english_words_alpha_set
import random
from PyDictionary import PyDictionary


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def do_you_want_to_play():
    while True:
        yn = input("Do you want to play hangman?? Y for yes, N for no").upper()
        if not(yn == "Y" or yn == "N"):
            print("Sorry, did not understand your response! Try again.")
            continue
        elif yn == "Y":
            return True
        else:
            return False


def do_you_want_to_play_again():
    while True:
        yn = input("Do you want to play again?? Y for yes, N for no").upper()
        if not(yn == "Y" or yn == "N"):
            print("Sorry, did not understand your response! Try again.")
        elif yn == "Y":
            return True
        else:
            return False


first_figure = (# initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """)


def hangman():
    word_list = list(english_words_alpha_set)
    word = random.choice(word_list)
    word_empty = list("_" * len(word))
    word_list = [i.upper() for i in word]
    guessed_letters = []
    guessed_letters_correct = []
    print(first_figure)
    tries = 6
    print(f"The word has {len(word)} letters.")
    try:
        dict = PyDictionary()
        n = 0
        for type, meaning in dict.meaning(word).items():
            print(f"The word is a {type}")
            for i in meaning:
                n += 1
                print(f"The meaning(s) are: {n}.{i}")
            print("\n")
    except:
        print("Sorry, no meaning available!!")
    while tries != 0:
        guess = input("Take a guess: ").upper()
        guessed_letters.append(guess)
        if guess in word_list:
            guessed_letters_correct.append(guess)
            word_index = word_list.index(guess)
            word_list[word_index] = "-"
            word_empty[word_index] = guess
            print(f"Hoorah, {guess} is in the word!")
            print(''.join(word_empty))
            if tries > 0 and "".join(guessed_letters_correct) == word.upper():
                print("\nHoorah, you have guessed the word!")
                print(f"The word is {word}")
                break
            else:
                pass
        elif len(guess) == len(word):
            if guess == word:
                print("\nHoorah, you guessed the word!")
                print(f"\nThe word is {word}")
                break
            else:
                tries -= 1
                print(f"{guess} is not the word!")
                print(f"You have {tries} tries left!")
        else:
            tries -= 1
            print(f"{guess} is not in the word!")
            print(f"You have {tries} tries left!")
        print(display_hangman(tries))
    if tries == 0:
        print("Out of turns, better luck next time!")
        print(f"The word was {word}")

def main():
    while True:
        if do_you_want_to_play():
            print("Let's play hangman!")
            hangman()
            if do_you_want_to_play_again():
                hangman()
            else:
                print("Have a great day ahead!")
                break
        else:
            print("Have a great day ahead!")
            break


if __name__ == "__main__":
    main()