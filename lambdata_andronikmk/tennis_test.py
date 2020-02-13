import unittest

from tennis import TennisPlayer

class TestStringMethods(unittest.TestCase):
    """Testing tennis class"""
    def test_winner(self):
        player = TennisPlayer('roger')
        
        self.assertEqual('The player has lost the match.', player.winner())


if __name__ == '__main__':
    unittest.main()
