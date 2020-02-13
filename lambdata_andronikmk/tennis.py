"""
Tennis Player Class
"""
import random

class TennisPlayer:
    """
    Tennis player statistics
    """
    def __init__(self, name):
        self.name = name
        self.age = random.randint(18, 38)
        self.fourhand_winners = random.randint(1, 42)
        self.backhand_winners = random.randint(1, 22)
        self.unforced_errors = random.randint(8, 50)
        self.aces = random.randint(1, 25)
        self.double_faults = random.randint(1, 15)

    def winner(self):
        a = self.unforced_errors
        b = self.fourhand_winners
        c = self.backhand_winners
        d = self.aces
        e = b + c + d
        if a > e:
            result = 'The player has lost the match.'
        else:
            result = 'The player has won the match.'
        return result
