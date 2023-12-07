"""
File: clear_bricks.py
Name: Sally 111613025
---------------------------------
A catch-bricks game
One brick drops at a time. User can catch it by clicking on it before it drops to the floor.
If user fails to catch it three times, game over :(
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GRect
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import random

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800
DELAY = 10
SIZE = 30
MIN_Y_SPEED = 2
MAX_Y_SPEED = 5

# initialize window and block
window = GWindow(WINDOW_WIDTH, WINDOW_HEIGHT)
block = GRect(SIZE, SIZE)
block.filled = True

# global variable, show if there is block in window
is_block = False


def main():
    """
    Dropping a block at a time from random x with random speed, while life > 0
    After user catches it or the current block drops out of window, drop a new one
    """
    global is_block
    onmouseclicked(remove_block)
    life = 3
    
    while life:
        
        # initialize random value for each round
        start_x = random.randint(0, window.width - block.width)
        speed = random.randint(MIN_Y_SPEED, MAX_Y_SPEED)
        
        # set is_block to True after adding it
        window.add(block, x=start_x, y=0)
        is_block = True
        
        while is_block:  # break when user catches it successfully
            block.move(0, speed)
            pause(DELAY)
            if block.y >= window.height:
                life -= 1
                break


def remove_block(event):
    """
    :param event: event.x, event.y shows the position user clicked on
    remove the block when user clicks on it
    """
    global is_block
    clicked_obj = window.get_object_at(event.x, event.y)
    if clicked_obj is not None:
        window.remove(clicked_obj)
        is_block = False  # set is_block to False after remove it


if __name__ == '__main__':
    main()
