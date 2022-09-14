class Card:
    def __init__(self, name, value):
        self._name = name
        self._value = value

    @property
    def name(self):
        return self._name
    
    @property
    def value(self):
        return self._value

    def __str__(self) -> str:
        return f"{self.name} {self.value}"

class Deck:
    def __init__(self):
        # create list for cards
        self._cards = []

        # TODO generate gards and shuffle deck
        self.create()

    def create(self):
        self._cards.clear()

        # common variables
        cards = [
            ["2", 2],
            ["3", 3],
            ["4", 4],
            ["5", 5],
            ["6", 6],
            ["7", 7],
            ["8", 8],
            ["9", 9],
            ["10", 10],
            ["King", 10],
            ["Queen", 10],
            ["Jack", 10],
            ["Ace", 11]
        ]

        names = ["Heart", "Club", "Diamond", "Spade"]

        for name in names:
            for card_data in cards:
                card_suit = name
                card_name = card_data[0]
                card_value = card_data[1]
                print(card_suit, card_name, card_value)

    def show(self):
        if not self._cards:
            print("There are no cards in this deck :(")
        else:
            print(self._cards)


deck = Deck()
deck.show()