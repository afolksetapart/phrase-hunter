import os
import random
import sys

from phrasehunter.character import Character
from phrasehunter.phrase import Phrase


class Game():
    def __init__(self, phrases):
        self.phrases = phrases
        self.random_phrase = random.choice(self.phrases)
        self.active_phrase = Phrase(self.random_phrase)
        self.current_score = self.active_phrase.num_correct
        self.already_guessed = []
        self.lives = 5

    def start_game(self):
        os.system('clear')
        print("\n?¿?¿ Welcome To Phrase Hunter ¿?¿?\n")
        self.new_game()

    def new_game(self):
        self.phrases.remove(self.random_phrase)

        while True:
            self.turn()
            self.update_score()

            if not self.lives:
                print(f"\n* you have {self.lives} out of 5 lives left *\n")
                self.active_phrase.print_phrase()
                print("\nGame Over! Better luck next time!\n")
                break

            elif self.current_score == len(self.active_phrase):
                print(f"\n* you have {self.lives} out of 5 lives left *\n")
                self.active_phrase.print_phrase()
                print("\nYou Win!\n")
                print(f"The phrase was ' {self.random_phrase} '\n")
                break

            else:
                continue

        if self.phrases:
            self.play_again()
        else:
            print("\nThat's all the phrases we have! Thanks for playing!\n")
            input("Press ENTER to exit...")
            sys.exit()

    def valid_guess(self, guess):
        while True:
            if len(guess) == 1 and guess.isalpha():
                if guess not in self.already_guessed:
                    self.already_guessed.extend((guess, guess.upper()))
                    break
                else:
                    guess = input(
                        "You already tried that letter, try again:  ")
                    continue
            else:
                guess = input("Not a valid guess, try again:  ")
                continue
        return guess

    def turn(self):
        print(f"\n* you have {self.lives} out of 5 lives left *\n")
        self.active_phrase.print_phrase()
        guess = input("\nGuess a letter:  ")

        guess = self.valid_guess(guess.lower())
        self.active_phrase.eval_guess(guess)

    def update_score(self):
        if self.active_phrase.num_correct == self.current_score:
            self.lives -= 1
            os.system('clear')
        elif self.active_phrase.num_correct > self.current_score:
            self.current_score = self.active_phrase.num_correct
            os.system('clear')
            print("Nice!")

    def play_again(self):
        while True:
            play_again = input("Would you like to play again? [y/n]  ")
            if play_again.isalpha():
                if play_again.lower() == "n":
                    sys.exit()
                elif play_again.lower() == "y":
                    os.system('clear')
                    self.reset_game()
                    self.new_game()
            else:
                continue

    def reset_game(self):
        self.random_phrase = random.choice(self.phrases)
        self.active_phrase = Phrase(self.random_phrase)
        self.current_score = self.active_phrase.num_correct
        self.already_guessed = []
        self.lives = 5
