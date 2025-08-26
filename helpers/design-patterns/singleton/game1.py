from leaderboard import Leaderboard
from interface_game import IGame


class Game1(IGame):
    """Game class"""

    def __init__(self):
        self.leaderboard = Leaderboard()

    def add_winner(self, position, name):
        """add winner implementation"""
        self.leaderboard.add_winner(position, name)
