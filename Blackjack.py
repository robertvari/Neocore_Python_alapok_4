import os
from game_assets.cards import Deck
from game_assets.players import AIPlayer, Player


class Blackjack:
    def __init__(self):
        # game intro
        self.intro()

        # create deck of cards
        self.deck = Deck()

        # TODO create player
        # TODO create AI Players
        # TODO Start first round

    def intro(self):
        self.clear_screen()
        print("="*50, "BLACKJACK", "="*50)
        print("Welcome to my game of Blackjack...")
        print("TODO game rules")
    
    def clear_screen(self):
        os.system("cls")

Blackjack()