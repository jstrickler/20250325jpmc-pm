# str bytes list dict tuple float bool set ...

class Card:   # inherits from 'object'
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def rank(self):  # getter property
        return self._rank
    # rank = property(rank)

    @rank.setter
    def rank(self, value):  # setter property   c.rank = "A"
        if isinstance(value, str):
            self._rank = value
        else:
            raise TypeError("rank must be a str")

    @property
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, value):
        self._suit = value
    
    def __str__(self):  # implements str() for this class
        return f"{self.rank}-{self.suit}"
    
    def __repr__(self):  # implements repr() for this class
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    # obj = ClassName(arg, ...)
    c = Card("8", 'Diamonds')
    print(type(c))
    print(c)   # print(str(c)) --> repr(c)
    print(c.rank, c.suit)
    # print(c._rank, c._suit)   # NAUGHTY!!
    # print(c.get_rank())
    c.rank = "A"
    print("str(c) ", str(c))
    print(f"repr(c) {repr(c)}")
