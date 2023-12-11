"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Name: Sally 111613025
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    game = BreakoutGraphics()
    life = NUM_LIVES
    
    # the animation loop, stop when life == 0 or brick_amount == 0
    while life and game.get_brick_amount():
        game.ball.move(game.get_ball_speed_x(), game.get_ball_speed_y())
        
        # check and change speed for all the collision between the ball, the bricks, the paddle, and the wall
        game.check_collision()
        
        if game.check_drop_out():  # if the ball drops out the window
            life -= 1
        pause(FRAME_RATE)
    
    # reset ball after the end of the game
    game.reset_ball()


if __name__ == '__main__':
    main()
