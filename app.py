# Import your Game class
from phrasehunter.game import Game
# Create your Dunder Main statement.
phrase_list = ["an apple a day", "the more the merrier", "hair in a biscuit",
               "lost at sea", "get what you give", "head in the clouds", "dancing in the moonlight"]


if __name__ == "__main__":
    game = Game(phrase_list)
    game.start_game()
# Inside Dunder Main:
# Create an instance of your Game class
# Start your game by calling the instance method that starts the game loop
