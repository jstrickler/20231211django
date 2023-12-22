from card import Card
from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for i in range(1,3):
            card = Card(f'JOKER{i}', f'JOKER{i}')
            self._cards.append(card)

if __name__ == "__main__":
    j1 = JokerDeck("Francesca")
    j1.shuffle()
    print(f"j1: {j1}")
    for _ in range(10):
        print(j1.deal())
    print(f"j1: {j1}")
    print(j1.cards)