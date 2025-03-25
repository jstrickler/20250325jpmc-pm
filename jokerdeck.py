from abc import ABCMeta, abstractmethod
from card import Card
from carddeck import CardDeck

class GameBase(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

    def scream(self):
        print("aieeeeeeee!!!")

class JokerDeck(GameBase, CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for joker_number in 1, 2:
            card = Card(f"JOKER-{joker_number}", "** JOKER **")
            self._cards.append(card)

    def scream(self):
        print("Run for your life!")

    def start(self):
        return super().start()
#        print("Starting...")

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    for i in range(10):
        print(j.draw())
    j.start()
    j.scream()
    print(JokerDeck.mro())