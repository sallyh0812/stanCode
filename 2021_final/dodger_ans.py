from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import random

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 340
MIN_SPEED = 2.0
MAX_SPEED = 4.0


class DodgerGraphics:
    def __init__(self, window_width=WINDOW_WIDTH,
                 window_height=WINDOW_HEIGHT):
        """
         Initializes the class attributes for the DodgerGraphics class. This
         class should keep track of the GWindow, the offset, the ball, and the
         square.
         """
        # Create a window with the correct width and height
        self.w = GWindow(width=window_width, height=window_height)
        # Create and place a filled ball in the graphical window
        # (part a)
        self.vx = random.randint(MIN_SPEED, MAX_SPEED)
        self.ball = GOval(window_height / 2, window_height / 2)
        self.ball.filled = True
        if random.random() > 0.5:
            self.w.add(self.ball, 0, 0)
        else:
            self.w.add(self.ball, 0, window_height / 2)
        # Create and place a filled square in the window
        # (part a)
        self.sq = GRect(window_height / 2, window_height / 2 - 1)
        self.sq.filled = True
        self.w.add(self.sq, self.w.width - self.sq.width, 0)
        # Initialize mouse listeners (part b)
        onmouseclicked(self.move_square)
    
    def move_square(self, event):
        """
        If the click is in the top half of the window, moves the square to the top left
        If the click is in the bottom half, moves the square to the bottom left corner
        """
        # Your Code Here
        if event.y < self.w.height / 2:
            self.w.add(self.sq, self.w.width - self.sq.width, 0)
        elif event.y > self.w.height / 2:
            self.w.add(self.sq, self.w.width - self.sq.width, self.w.height / 2)
    
    def reset_ball(self):
        """
        Resets the ball's x speed to a random positive speed and places the ball
        randomly in either the top half or the bottom half of the window, with its left side
        against the left wall.
        """
        # Your Code Here
        self.vx = random.randint(MIN_SPEED, MAX_SPEED)
        if random.random() > 0.5:
            self.w.add(self.ball, 0, 0)
        else:
            self.w.add(self.ball, 0, self.w.height / 2)


FRAME_RATE = 10


def main():
    # Your Code Here
    g = DodgerGraphics()
    while True:
        pause(FRAME_RATE)
        g.ball.move(g.vx, 0)
        if g.w.get_object_at(g.ball.x + g.ball.width, g.ball.y + g.ball.height / 2) is g.sq:
            g.w.remove(g.ball)
            g.w.remove(g.sq)
            break
        if g.ball.x + g.ball.width >= g.w.width:
            g.reset_ball()


if __name__ == '__main__':
    main()
