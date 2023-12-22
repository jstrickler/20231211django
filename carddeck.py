import random
from card import Card

class CardDeck:
    ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    suits = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer) -> None:
        self.dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = list()
        for suit in self.suits:
            for rank in self.ranks:
                card = Card(rank, suit)
                self._cards.append(card)
        

    @property
    def cards(self):
        return tuple(self._cards)

    @property
    def dealer(self):
        return self._dealer
    
    @dealer.setter
    def dealer(self, value):
        if isinstance(value, str):
            self._dealer = value
        else:
            raise TypeError("Dealer must be a string")

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self):
        return self._cards.pop()

    def __len__(self):
        return len(self._cards)
    
    def __str__(self):
        return f"CardDeck:{len(self)}"
    
    def __repr__(self):
        return f"CardDeck('{self.dealer}')"
        

if __name__ == "__main__":
    d1 = CardDeck("Mathilda")
    print(f"d1: {d1}")
    d1.shuffle()
    print(d1.cards)
    print()
    print(f"len(d1): {len(d1)}")
    print(f"repr(d1): {repr(d1)}")
    for _ in range(5):
        card = d1.deal()
        print(f"card: {card}")
    print(f"d1: {d1}")
    print(f"len(d1): {len(d1)}")
    