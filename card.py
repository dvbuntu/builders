from player import player

class card:
    '''
    Basic class for a card.  Resources can be raw, manufactured, money, points,
    or military strength.
    '''
    def __init__(self, name, resources = defaultdict(int)):
        self.name = name
        self.resources = resources
