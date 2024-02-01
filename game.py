import numpy as np
import random
from board import Board  # Assuming there's a custom Board class defined in the 'board' module
import keyboard
import time

def configure_game():
    
    max_gen = int(input("Enter the maximum number of generations (0 for unlimited): "))
    #You can add all the confiogurations you need
    return max_gen



def Run():
    max_gen = configure_game()    
    start = time.time()

    myboard = Board()  # Creating an instance of the Board class
    stop = False
    while not keyboard.is_pressed('Escape') and (max_gen == 0 or myboard.generation < max_gen):
        if (time.time() - start) >= 0.5:
            print(myboard)  # Displaying the current state of the board
            myboard.Actualize()  # Updating the board state
            start = time.time()
    print("End of the iterations")
    # Prompt the user to press Enter to continue
    input("Press Enter to close the console...")

Run()
