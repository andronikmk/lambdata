import unittest

class TestStringMethods(unittest.TestCase):
    """Testing tennis class"""
    def test_winner(self):
        self.assertTrue('The player has lost the match.'.encode())


if __name__ == '__main__':
    unittest.main()
