"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Name: Sally 111613025
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    life = NUM_LIVES

    # Add the animation loop here!
    while life and graphics.brick_amount:
        graphics.ball.move(graphics.get_ball_speed_x(), graphics.get_ball_speed_y())
        if graphics.check_collision() == "drop out":
            life -= 1
        pause(FRAME_RATE)
    graphics.reset_ball()


if __name__ == '__main__':
    main()
