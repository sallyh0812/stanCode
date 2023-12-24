from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)
    vx = VX
    vy = 0
    while ball.x < window.width:
        vy += GRAVITY
        ball.move(vx, vy)
        if ball.y + ball.height >= window.height and vy > 0:
            vy = -vy * REDUCE
        pause(DELAY)


if __name__ == '__main__':
    main()