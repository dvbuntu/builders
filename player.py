'''
Class and associated content for Builders players.
'''
from collections import defaultdict

class player:
    self.resources = defaultdict(int)
    self.points = self.resources['points']
    def __init__(self, name, human = True):
        self.name = name
        self.human = human
    def set_neighbors(self, left, right):
        self.left = left
        self.right = right
