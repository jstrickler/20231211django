
VALID_SUITS = ""

class Card:  # inherits from 'object' -- supports str() and bool()
    def __init__(self, rank, suit):    # 'self':Python::'this':Java
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):   # public variable for ._rank
        return self._rank

    @property
    def suit(self):  # getter property
        return self._suit
    
    @suit.setter
    def suit(self, value):  # setter property
        self._suit = value

    def __str__(self): # user-friendly representation of object
        return f"{self.rank}-{self.suit}"

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = Card('5', 'Diamonds')
    print(f"c1.rank: {c1.rank}")
    print(f"c1.suit: {c1.suit}")
    c1.suit = "Honeybees"
    print(f"c1.rank: {c1.rank}")
    print(f"c1.suit: {c1.suit}")

    print(c1)
    print(repr(c1))

    c2 = Card('Q', 'Spades')
    print(f"c2: {c2}")
    print(f"repr(c2): {repr(c2)}")
    