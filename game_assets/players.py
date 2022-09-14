import random, time

class Player_Base:
    def __init__(self):
        self._name = None
        self._credits = 0
        self._hand = []
        self._in_game = True

        self.create()
    
    def create(self):
        first_names = ["Brittney", "Curtis", "Lucas", "Chip", "Simon"]
        last_names = ["Moriah", "Tristin", "Troy", "Gale", "Lynn"]
        self._name = f"{random.choice(first_names)} {random.choice(last_names)}"

        self._credits = random.randint(10, 100)

    @property
    def full_name(self):
        return self._name

    @property
    def credits(self):
        return self._credits

    def draw_card(self, deck):
        while self._in_game:
            # count hand
            if self.count_hand < random.randint(16, 19):
                print(f"{self.full_name} draws a card")
                time.sleep(random.uniform(0.5, 2))

                my_new_card = deck.give_card()

                if self.count_hand > 10 and my_new_card.value == 11:
                    my_new_card.value = 1

                self._hand.append(my_new_card)
            else:
                print(f"{self.full_name} passes...\n")
                time.sleep(random.uniform(0.5, 2))
                self._in_game = False

    def init_hand(self, deck):
        self._hand.clear()
        self._in_game = True

        new_card = deck.give_card()
        self._hand.append(new_card)

        new_card = deck.give_card()

        if self.count_hand > 10 and new_card.value == 11:
            new_card.set_value(1)
        self._hand.append(new_card)

    @property
    def count_hand(self):
        # count = 0
        # for card in self._hand:
        #     count += card.value

        return sum([card.value for card in self._hand])

    @property
    def status(self):
        print(f"{self._name} Hand: {self._hand} Hand Value: {self.count_hand}")

    def show_hand(self):
        print(self._hand)

    def __str__(self) -> str:
        return f"{self._name}"

    def __repr__(self) -> str:
        return f"{self._name}"

class Player(Player_Base):
    # overrides create() from base class
    def create(self):
        # runs base class create()
        super().create()
        # self._name = input("What is your  name?")
        self._name = "Robert Vari"

    def draw_card(self, deck):
        print(f"This is your turn {self._name.split()[0]}")

        while self._in_game:
            self.show_hand()
            print(f"Your hand value is: {self.count_hand}")

            if self.count_hand >= 21:
                self._in_game = False
                print("You passes...")

                if self.count_hand > 21:
                    print("You lost this tudn... :(")
                break
            
            user_input = input("Do you want to draw a new card? (y/n)")
            if user_input == "y":
                new_card = deck.give_card()
                print(f"Your new card: {new_card}")

                if self.count_hand > 10 and new_card.value == 11:
                    new_card.value = 1
                
                self._hand.append(new_card)
            else:
                self._in_game = False

class AIPlayer(Player_Base): 
    pass


# testing players
if __name__ == "__main__":
    from cards import Deck
    deck = Deck()

    player = Player()
    player.init_hand(deck)
    player.draw_card(deck)