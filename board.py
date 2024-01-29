import numpy as np
import random

class Board:
    def __init__(self, size=20, initial_state=1):
        if isinstance(initial_state, int)==False: 
            self.size = initial_state.shape[0]
            self.board = initial_state
        else:
            self.size = size
            self.board = np.zeros((self.size, self.size*2))

    def __str__(self):
        rep = " "
        rep += "-" * self.size*2
        rep += "\n"
        for i in range(self.size):
            rep += "|"
            for j in range(self.size*2):
                rep += "#" if self.board[i, j]==1 else " "
            rep += "|\n"
        rep += " "
        rep += "-" * self.size*2
        return rep

    def Get_neighbors(self, x, y):
        cnt=0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if x+i >= 0 and x+i < self.size and y+i >= 0 and y+i < self.size*2:
                    if self.board[x+i, y+i]==1: cnt+=1
        return cnt

    def Changes(self):
        changes = np.zeros((self.size, self.size*2))
        for i in range(self.size):
            for j in range(self.size*2):
                if self.board[i, j]==1 and (self.Get_neighbors(i,j)<2 or self.Get_neighbors(i,j)>3):
                    changes[i, j]=1
                if self.board[i, j]==0 and self.Get_neighbors(i,j)==3:
                    changes[i, j]=1
        return changes

    def Actualize(self):
        changes = self.Changes()
        for i in range(self.size):
            for j in range(self.size*2):
                self.board[i, j] = 1 - self.board[i, j] if changes[i, j]==1 else self.board[i, j]