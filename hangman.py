# importing required packages
from english_words import english_words_alpha_set
import random


def do_you_want_to_play():
    while True:
        yn = input("Do you want to play hangman?? Y for yes, n for no").upper()
        if not(yn == "Y" or yn == "N"):
            print("Sorry, did not understand your response! Try again.")
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


def hangman():
    word_list = list(english_words_alpha_set)
    word = random.choice(word_list)
    print(word)
    word = word.upper()
    word_empty = list("_" * len(word))
    word_letters = [i.upper() for i in word]
    guessed_letters = []
    print(f"The encoded word is: {''.join(word_empty)}")
    tries = 6
    guessed = True
    while guessed and tries != 0:
        guess = input("Take a guess:").upper()
        if guess in word_letters:
            guess_index = word_letters.index(guess)
            word_letters[guess_index] = "-"
            word_empty[guess_index] = guess
            print("".join(word_empty))
            guessed_letters.append(guess)
            if "".join(guessed_letters) == word:
                print("You have won the game! Congrats.")
                print(f"The word is {word}")
                guessed = False
            else:
                pass
        elif len(word) == len(guess):
            if guess == word:
                print("Booyah! You won the game.")
                print(f"The word is {word}")
                guessed = False
            else:
                tries -= 1
                print(f"Sorry, {guess} is not the word.")
                continue
        else:
            tries -= 1
            print(f"Sorry, {guess} is not in the word.")
            continue
    if tries == 0:
        print("Out of turns, better luck next time!!")


def main():
    while True:
        if do_you_want_to_play():
            hangman()
            if do_you_want_to_play_again():
                hangman()
            else:
                break
        else:
            break


if __name__ == "__main__":
    main()