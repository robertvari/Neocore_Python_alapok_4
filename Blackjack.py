import os, random
from game_assets.cards import Deck
from game_assets.players import AIPlayer, Player


class Blackjack:
    def __init__(self):
        # game intro
        self.intro()

        # create deck of cards
        self.deck = Deck()

        # create player and create AI Players
        self.players = [
            Player(),
            AIPlayer(),
            AIPlayer(),
            AIPlayer()
        ]

        # Start first round
        self.start_round()

    def start_round(self):
        self.clear_screen()

        # reset deck
        self.deck.create()

        # shuffle player list
        random.shuffle(self.players)

        # reset player hands
        for p in self.players:
            p.init_hand(self.deck)

        for p in self.players:
            p.draw_card(self.deck)

        print("-"*50, "Game Status", "-"*50)
        for p in self.players:
            p.status

    def intro(self):
        self.clear_screen()
        print("="*50, "BLACKJACK", "="*50)
        print("Welcome to my game of Blackjack...")
        print("TODO game rules")
    
    def clear_screen(self):
        os.system("cls")

Blackjack()