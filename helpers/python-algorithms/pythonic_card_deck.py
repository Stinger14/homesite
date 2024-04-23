import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class CustomDeck:
    """
    A class representing a custom deck of cards.

    Attributes:
        ranks (list): A list of card ranks.
        suits (list): A list of card suits.
        _cards (list): A list of Card objects representing the deck of cards.

    Methods:
        __init__(): Initializes a new instance of the CustomDeck class.
        __len__(): Returns the number of cards in the deck.
        __getitem__(position): Returns the card at the specified position in the deck.
    """

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = CustomDeck()
print(len(deck))
