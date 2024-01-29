import numpy as np
import random
from board import Board
import keyboard
import time

def Run():
    start = time.time()
    myboard = Board()
    stop = False
    while keyboard.is_pressed('Escape')==False:
        if (time.time() - start) >= 0.5:
            print(myboard)
            myboard.Actualize()
            start = time.time()

Run()