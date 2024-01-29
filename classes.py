import numpy as np
import random

class Board:
    def __init__(self, size=20, initial_state=1):
        self.size = size
        if isinstance(initial_state, int)==False: self.board = initial_state
        else:
            self.board = np.zeros((self.size, self.size*2))

    def __str__(self):
        rep = " "
        rep += "-" * self.size*2
        rep += "\n"
        for i in range(self.size):
            rep += "|"
            for j in range(self.size*2):
                rep += "#" if self.board[i,j]==1 else " "
            rep += "|\n"
        rep += " "
        rep += "-" * self.size*2
        return rep

state = np.zeros((20,40))
for i in range(20): 
    for j in range(40): state[i, j] = random.randint(0,1)
myboard = Board(initial_state=state)
print(myboard)