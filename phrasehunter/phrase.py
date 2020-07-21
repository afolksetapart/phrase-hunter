from phrasehunter.character import Character


class Phrase(list):
    def __init__(self, phrase):
        self.phrase = phrase

        for char in self.phrase:
            self.append(Character(char))

        for char in self:
            if char.original == " ":
                char.was_guessed = True

    def eval_guess(self, guess):
        for char in self:
            char.check_guess(guess)

    def print_phrase(self):
        display_string = ""
        for char in self:
            display_string += char.display_char()
        print(display_string)

    @property
    def num_correct(self):
        correct = 0
        for char in self:
            if char.was_guessed == True:
                correct += 1
        return correct
