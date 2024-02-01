import numpy as np
import random
from board import Board
import keyboard
import time

def Run(board_size):
    initial_state = 1
    custom_state = input("Do you want to go with a random start ? (y/N)")
    if custom_state.upper() == "N":
        size, initial_state = CustomBoard()
        
    max_gen = int(input("Enter the maximum number of generations (0 for unlimited): "))
    start = time.time()
    myboard = Board(size = board_size, initial_state = initial_state)
    stop = False
    while not keyboard.is_pressed('Escape') and (max_gen == 0 or myboard.generation < max_gen):
        if (time.time() - start) >= 0.5:
            print(myboard)
            myboard.Actualize()
            start = time.time()
    print("End of the iterations")
    # Prompt the user to press Enter to continue
    input("Press Enter to close the console...")
    
def CustomBoard():
    size = int(input("Choose the grid size (5 for 2*5 x 5 grid)"))
    initial_state = np.zeros((size, size*2))

    # Get user input for the initial state
    for i in range(size):

        row_input = input(f"Enter row {i + 1} (use 0 and 1, e.g., '010101'): ")
        while len(row_input)!=size*2:
            print("You need to enter a", size*2, "sized chain")
            row_input = input(f"Enter row {i + 1} (use 0 and 1, e.g., '010101'): ")
            
        initial_state[i] = [int(cell) for cell in row_input]
    
    return size, initial_state
Run(20)
