from game1 import Game1
from game2 import Game2
from game3 import Game3

GAME1 = Game1()
GAME1.add_winner(2, "Max")

GAME2 = Game2()
GAME2.add_winner(1, "Maxly")

GAME3 = Game3()
GAME3.add_winner(3, "Diana")

GAME1.leaderboard.print() 
GAME2.leaderboard.print() 
GAME3.leaderboard.print()