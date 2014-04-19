'''
Class and associated content for Builders players.
'''
from collections import defaultdict

class player:
    self.resources = defaultdict(int)
    def __init__(self, name, human = True):
        self.name = name
        self.human = human
        self.cards = list()
    def set_neighbors(self, left, right):
        self.left = left
        self.right = right
    @property
    def points(self):
        return self.resources['points']
    @points.setter
    def points(self, value):
        self.resources['points'] = value
    @property
    def dollars(self):
        return self.resources['dollars']
    @dollars.setter
    def dollars(self, value):
        self.resources['dollars'] = value
