"""
File: bouncing_ball.py
Name: Sally 111613025
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# initialize window and ball
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
ball.filled = True

# show how many times has the ball dropped out of window
out = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(drop_ball)


def drop_ball(event):
    """
    Drop the ball after user click on the window.
    Do nothing if ball is not at the start point or has dropped out three times already.
    """
    global out
    
    # do nothing if ball is not at the start point or has dropped out three times already
    if window.get_object_at(START_X + ball.width / 2, START_Y + ball.height / 2) is not None and out < 3:
        vy = 0
        while ball.x <= window.width:
            if ball.y + ball.height >= window.height and vy >= 0:  # make sure vy < 0 (go up) after bounced
                vy = -vy * REDUCE  # *REDUCE after each bounce
            vy += GRAVITY
            ball.move(VX, vy)
            pause(DELAY)
        
        # when the ball dropped out
        out += 1
        window.add(ball, x=START_X, y=START_Y)


if __name__ == "__main__":
    main()
