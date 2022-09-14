import random


class Card:
    def __init__(self, name: str, value: int):
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

    def __repr__(self) -> str:
        return f"{self.name} {self.value}"


class Deck:
    def __init__(self):
        # create list for cards
        self._cards = []

        # generate gards and shuffle deck
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
            
                self._cards.append(
                    Card(f"{card_suit} {card_name}", card_value)
                )
        
        random.shuffle(self._cards)

    def give_card(self):
        new_card = self._cards[0]
        self._cards.remove(new_card)
        return new_card

    def show(self):
        if not self._cards:
            print("There are no cards in this deck :(")
        else:
            for i in self._cards:
                print(i)


# runs only when this file is executed
if __name__ == "__main__":
    deck = Deck()