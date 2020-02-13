"""
Tennis Player Class
"""
import random

class TennisPlayer():
    """
    Tennis player statistics
    """
    def __init__(self, name, age=1,
                 fourhand_winner=1, backhand_winner=1,
                 unforced_error=1, aces=1, double_faults=1):
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
            print('The player has lost the match.')
        else:
            print('The player has won the match.')
