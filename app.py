
from phrasehunter.game import Game

phrase_list = ["an apple a day", "the more the merrier", "hair in a biscuit",
               "lost at sea", "get what you give", "head in the clouds", "dancing in the moonlight"]


if __name__ == "__main__":
    game = Game(phrase_list)
    game.start_game()
