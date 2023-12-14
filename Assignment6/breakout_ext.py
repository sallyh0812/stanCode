"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Name: Sally 111613025
"""

from campy.gui.events.timer import pause
from breakoutgraphics_ext import BreakoutGraphicsExt

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 5  # Number of attempts


def main():
    game = BreakoutGraphicsExt()
    life = NUM_LIVES
    #
    game.window.add(game.rule)
    pause(3000)
    game.window.remove(game.rule)
    # the animation loop, stop when life == 0 or brick_amount == 0
    while life and game.get_brick_amount():
        game.ball.move(game.get_ball_speed_x(), game.get_ball_speed_y())
        
        game.add_tools()
        
        # check and change speed for all the collision between the ball, the bricks, the paddle, and the wall
        game.check_game_ball1()
        
        if game.ball2 is not None:
            game.ball2.move(game.get_ball2_speed_x(), game.get_ball2_speed_y())
            game.check_game_ball2()
            game.check_drop_out2()
            
        if game.is_long_paddle:
            if not game.long_paddle_time:
                game.reset_paddle_width()
        if game.is_free_paddle:
            if not game.free_paddle_time:
                game.unfree_paddle()
                
        if game.is_short_paddle:
            if not game.short_paddle_time:
                game.reset_paddle_width()
        
        if game.check_drop_out1():  # if the ball drops out the window
            life -= 1
        pause(FRAME_RATE)
        
    if not life:
        game.fail()
    else:
        game.success()
    
    # reset ball after the end of the game
    game.reset_ball()


if __name__ == '__main__':
    main()
