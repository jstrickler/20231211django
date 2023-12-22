
class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    @rank.setter
    def rank(self, value):
        pass

    def __repr__(self):
        return f"Card('{self._rank}', '{self._suit}')"

    def __str__(self):
        return f"{self.rank}-{self.suit}"
    
    def __eq__(self, other):
        return (self.rank == other.rank) and (self.suit == other.suit)

    def __hash__(self):
        hash_key = self.rank, self.suit  # key is tuple of rank and suit
        return hash(hash_key) # compute hash key on uniquie rank/suit combo
     

if __name__ == "__main__":
    c1 = Card('2', 'Clubs')
    c2 = Card('2', 'Clubs')
    c3 = Card('3', 'Clubs')

    print(c1 == c2)
    print(c1 == c3)
