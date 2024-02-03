import numpy as np
import random

class Board:
    def __init__(self, size=20, initial_state=1):
        self.generation = 0  # Initialize generation counter
        if isinstance(initial_state, int)==False: 
            self.size = initial_state.shape[0]
            self.board = initial_state
        else:
            self.size = size
            self.board = np.zeros((self.size, self.size*2))
            for i in range(self.size):
                for j in range(self.size*2):
                    self.board[i, j] = random.randint(0, 1)

    def __str__(self):
        rep = "Generation: " + str(self.generation + 1) + "\n "  # Display the current generation
        rep += "-" * self.size*2
        rep += "\n"
        for i in range(self.size):
            rep += "|"
            for j in range(self.size*2):
                rep += "▪" if self.board[i, j]==1 else " "
            rep += "|\n"
        rep += " "
        rep += "-" * self.size*2
        return rep

    def Get_neighbors(self, x, y):
        cnt=0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if x+i >= 0 and x+i < self.size and y+j >= 0 and y+j < self.size*2:
                    if i!=0 or j!=0:
                        if self.board[x+i, y+j]==1: 
                            cnt+=1
        return cnt

    def Changes(self):
        changes = np.zeros((self.size, self.size*2))
        for i in range(self.size):
            for j in range(self.size*2):
                neighbors = self.Get_neighbors(i, j)
                if self.board[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                    changes[i, j] = 1
                if self.board[i, j] == 0 and neighbors == 3:
                    changes[i, j] = 1
        return changes

    def Actualize(self):
        changes = self.Changes()
        for i in range(self.size):
            for j in range(self.size*2):
                self.board[i, j] = 1 - self.board[i, j] if changes[i, j]==1 else self.board[i, j]
        self.generation += 1  # Increment the generation counter after each update
