# Create your Character class logic in here.

class Character():
    def __init__(self, original, was_guessed=False):
        self.original = original
        self.was_guessed = was_guessed

    def check_guess(self, guess):
        if guess == self.original:
            self.was_guessed = True

    def display_char(self):
        if self.was_guessed == True:
            return self.original + " "
        else:
            return "_ "
