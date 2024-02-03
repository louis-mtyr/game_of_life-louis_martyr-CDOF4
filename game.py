import numpy as np
import random
from board import Board  # Assuming there's a custom Board class defined in the 'board' module
import keyboard
import time

def configure_game():
    print("What size of board do you want to use ? (The format will be n x 2n)")
    board_size = input("Pick a positive integer: ")
    while board_size.isnumeric()==False:
        board_size = input("Pick a positive integer: ")
    board_size = int(board_size)
    initial_state = 1
    custom_state = input("Do you want to go with a random start ? (Y/n)")
    if custom_state.upper() == "N":
        initial_state = CustomBoard(board_size)
        
    max_gen = int(input("Enter the maximum number of generations (0 for unlimited): "))
    #You can add all the confiogurations you need
    return max_gen, initial_state, board_size

def Run():
    max_gen, initial_state, board_size = configure_game()    
    start = time.time()
    myboard = Board(size = board_size, initial_state = initial_state)
    stop = False
    while not keyboard.is_pressed('Escape') and (max_gen == 0 or myboard.generation < max_gen):
        if (time.time() - start) >= 0.5:
            print(myboard)  # Displaying the current state of the board
            myboard.Actualize()  # Updating the board state
            start = time.time()
    print("End of the iterations")
    # Prompt the user to press Enter to continue
    input("Press Enter to close the console...")
    
def CustomBoard(size):
    initial_state = np.zeros((size, size*2))

    # Get user input for the initial state
    for i in range(size):

        row_input = input(f"Enter row {i + 1} (use 0 and 1, e.g., '010101'): ")
        while len(row_input)!=size*2:
            print("You need to enter a", size*2, "sized chain")
            row_input = input(f"Enter row {i + 1} (use 0 and 1, e.g., '010101'): ")
            
        initial_state[i] = [int(cell) for cell in row_input]
    
    return initial_state

Run()