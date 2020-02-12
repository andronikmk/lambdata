"""
Classes to represent games.
"""
from random import random

class Game:
    """
    General represent of an abstract game.
    """
    fun_level = 5

    def __init__(self, player1='Alice', player2='Bob'):
        self.rounds = 2
        self.current_round = 0
        self.player1 = player1
        self.player2 = player2

    def print_players(self):
        """Print the players of the game."""
        print('{} is playing {}'.format(self.player1, self.player2))

    def add_round(self):
        self.rounds += 1

    def winner(self):
        """Randomly pick and return winner of game."""
        return self.player1 if random() > 0.5 else self.player2

class TicTacToe(Game):
    """TicTacToe game representation."""
    def __init__(self, player1='Will', player2='Mac'):
        super().__init__(player1, player2)
        self.rounds = 3
        

    def print_players(self):
        print('{} is playing Tic-Tac-Toe with {}'.format(self.player1, self.player2))
