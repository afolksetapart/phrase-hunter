import os
import random
import sys

from phrasehunter.character import Character
from phrasehunter.phrase import Phrase


class Game():
    def __init__(self, phrases):
        self.phrases = phrases

    def start_game(self):
        os.system('clear')
        print("\n?¿?¿ Welcome To Phrase Hunter ¿?¿?\n")

        while True:
            random_phrase = random.choice(self.phrases)
            active_phrase = Phrase(random_phrase)
            self.phrases.remove(random_phrase)
            already_guessed = []
            lives = 5

            while True:
                current_score = active_phrase.num_correct
                print(f"\n* you have {lives} out of 5 lives left *\n")
                active_phrase.print_phrase()

                guess = input("\nGuess a letter:  ")
                guess = guess.lower()
                guess = self.valid_guess(guess, already_guessed)

                active_phrase.eval_guess(guess)

                if active_phrase.num_correct == current_score:
                    lives -= 1
                    if lives > 0:
                        os.system('clear')
                        continue
                    elif lives == 0:
                        print("\nBetter luck next time!\n")
                        break

                elif active_phrase.num_correct > current_score:
                    if active_phrase.num_correct == len(active_phrase):
                        os.system('clear')
                        print("Nice!")
                        print(f"\n* you have {lives} out of 5 lives left *\n")
                        active_phrase.print_phrase()
                        print("\nYou Win!\n")
                        print(f"The phrase was ' {random_phrase} '\n")
                        break
                    else:
                        os.system('clear')
                        print("Nice!")
                        continue

            if len(self.phrases) == 0:
                print("\nThat's all the phrases we have! Thanks for playing!\n")
                input("Press ENTER to exit...")
                sys.exit()

            while True:
                play_again = input("Would you like to play again? [y/n]  ")
                if play_again.isalpha():
                    play_again.lower()
                    if play_again == "n":
                        sys.exit()
                    elif play_again == "y":
                        break
                else:
                    continue
            os.system('clear')
            continue

    @staticmethod
    def valid_guess(guess, guess_list):
        while True:
            if len(guess) == 1 and guess.isalpha():
                if guess not in guess_list:
                    guess_list.extend((guess, guess.upper()))
                    break
                else:
                    guess = input(
                        "You already tried that letter, try again:  ")
                    continue
            else:
                guess = input("Not a valid guess, try again:  ")
                continue
        return guess
