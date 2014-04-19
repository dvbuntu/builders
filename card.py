from player import player

class card:
    '''
    Basic class for a card.  Resources can be raw, manufactured, money, points,
    or military strength.
    '''
    def __init__(self, name,
                 resources = defaultdict(int),
                 prereq = None,
                 postreq = None,
                 era = 1):
        self.name = name
        self.resources = resources

def make_dollar_card(name, num_dollars):
    return card(name, defaultdict(int, ('dollars', num_dollars)))

def make_rock_card(name, num_rocks):
    return card(name, defaultdict(int, ('rocks', num_rocks)))

def make_point_card(name, num_points):
    return card(name, defaultdict(int, ('points', num_points)))

buildings = [make_point_card('shack',1),
             make_point_card('shed',2),
             make_dollar_card('nickel',5),
             make_rock_card('quarry',1)]
