# Create your Phrase class logic here.
#from phrasehunter.character import Character


class Phrase(list):
    def __init__(self, phrase):
        self.phrase = phrase

        for char in self.phrase:
            self.append(Character(char))

    def eval_guess(self, guess):
        for char in self:
            char.check_guess(guess)

    def print_phrase(self):
        display_string = ""
        for char in self:
            display_string += char.display_char()
        print(display_string)
