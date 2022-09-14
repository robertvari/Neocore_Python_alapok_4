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


class Player(Player_Base):
    pass

class AIPlayer(Player_Base):    
    pass


# testing players
if __name__ == "__main__":
    ai_player = AIPlayer()