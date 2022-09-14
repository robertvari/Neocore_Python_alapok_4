import os, random, time
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


        self.get_winner()

    def get_winner(self):
        self.clear_screen()
        print("-"*50, "Get Winner", "-"*50)
        time.sleep(2)

        players_in_turn = [player for player in self.players if player.count_hand <= 21]

        if not players_in_turn:
            print("Nobody wins this time.")
        else:
            winner_list = sorted(players_in_turn, key= lambda p: p.count_hand)

            whinner = winner_list [-1]
            print(f"The winner is: {whinner}")
        
        player_input = input("Do you want to play a new round? (y/n)")

        if player_input == "y":
            self.start_round()
        else:
            print("See you later!")
            exit()

    def intro(self):
        self.clear_screen()
        print("="*50, "BLACKJACK", "="*50)
        print("Welcome to my game of Blackjack...")
        print("TODO game rules")
    
    def clear_screen(self):
        os.system("cls")

Blackjack()