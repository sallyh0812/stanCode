"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Name: Sally 111613025
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 5  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 8  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 4  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball
SCORE_FONT = "-20"
SCORE_OFFSET = 8
STATUS_BOARD_HEIGHT = 50
LONG_PADDLE_TIME = 5
IMG_FILE = "mole.png"


class Brick(GRect):
    def __init__(self, brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT, brick_life=4):
        super().__init__(width=brick_width, height=brick_height)
        self.brick_life = brick_life
        self.filled = True
        if self.brick_life == 4:
            self.brick_color = 'black'
        elif self.brick_life == 3:
            self.brick_color = 'darkgray'
        elif self.brick_life == 2:
            self.brick_color = 'lightgray'
        elif self.brick_life == 1:
            self.brick_color = 'firebrick'
        self.fill_color = self.brick_color


class BreakoutGraphics_ext:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 status_board_height=STATUS_BOARD_HEIGHT, score_font=SCORE_FONT, score_offset=SCORE_OFFSET,
                 img_file=IMG_FILE, title='Breakout'):
        """
        Make the initial window with some bricks, a ball, a paddle, and start the mouse listener
        """
        
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing) + paddle_offset
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Default score board
        self.score = 0
        self.score_board = GLabel(f"Score: {self.score}")
        self.score_board.font = score_font
        self.score_board.color = 'white'
        # Default life board
        self.life = 3
        self.life_board = GLabel(chr(10084)*self.life)
        self.life_board.font = score_font
        self.life_board.color = 'white'
        
        # img
        # self.img = GImage(img_file)
        # self.window.add(self.img, x=0, y=brick_offset)
        
        # status board
        self.status_board_height = self.score_board.height * 2
        self.status_board = GRect(window_width, status_board_height, x=0, y=window_height - self.status_board_height)
        self.status_board.filled = True
        self.status_board.fill_color = 'firebrick'
        self.window.add(self.status_board)
        self.window.add(self.score_board, x=score_offset, y=self.window.height - score_offset)
        self.window.add(self.life_board, x=self.window.width - self.life_board.width - score_offset,
                        y=self.window.height - score_offset)
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width - self.paddle.width) / 2,
                        y=self.window.height - paddle_offset - self.status_board_height)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)
        
        # Default initial velocity for the ball
        self.__ball_dx = 0
        self.__ball_dy = 0
        
        # Draw bricks
        current_y = brick_offset
        self.brick_color = 'gray'
        for i in range(brick_rows):
            current_x = 0
            for j in range(brick_cols):
                self.brick = Brick(brick_life=random.randint(1, 4))
                self.window.add(self.brick, x=current_x, y=current_y)
                current_x += self.brick.width + brick_spacing
            current_y += self.brick.height + brick_spacing
        
        # Default initial bricks amount
        self.__brick_amount = brick_cols * brick_rows
        
        # shop
        self.double_ball = GRect(20, 20)
        self.double_ball.filled = True
        self.double_ball.fill_color = 'green'
        self.window.add(self.double_ball, x=0, y=0)
        
        self.longer_paddle = GRect(20, 20)
        self.longer_paddle.filled = True
        self.longer_paddle.fill_color = 'yellow'
        self.window.add(self.longer_paddle, x=25, y=0)
        
        self.shorten_paddle = GRect(20, 20)
        self.shorten_paddle.filled = True
        self.shorten_paddle.fill_color = 'red'
        self.window.add(self.shorten_paddle, x=50, y=0)
        
        self.free_paddle = GRect(20, 20)
        self.free_paddle.filled = True
        self.free_paddle.fill_color = 'blue'
        self.window.add(self.free_paddle, x=75, y=0)
        
        # self.double_score = GRect(20, 20)
        # self.double_score.filled = True
        # self.double_score.fill_color = 'purple'
        # self.window.add(self.double_score, x=100, y=0)
        
        #
        self.ball2 = None
        self.__ball2_dx = 0
        self.__ball2_dy = 0
        
        #
        self.is_long_paddle = False
        self.long_paddle_time = LONG_PADDLE_TIME
        
        #
        self.is_free_paddle = False
        
        #
        self.paddle_area_lower = self.paddle.y
        self.paddle_area_upper = self.ball.y + paddle_offset
        
        # Initialize our mouse listeners
        onmouseclicked(self.set_ball_speed)
        onmousemoved(self.move_paddle)
    
    
    def update_brick(self, current_brick):
        if current_brick.brick_life != 1:
            new_brick = Brick(brick_life=current_brick.brick_life - 1)
            self.window.add(new_brick, x=current_brick.x, y=current_brick.y)
        else:
            self.__brick_amount -= 1
        self.window.remove(current_brick)
    
    def move_paddle(self, mouse):
        """
        Set paddle.x to current mouse.x
        """
        if self.is_free_paddle:
            if mouse.y - self.paddle.height / 2 < self.paddle_area_upper:  # right boundary
                self.paddle.y = self.paddle_area_upper
            elif mouse.y - self.paddle.height / 2 > self.paddle_area_lower:  # left boundary
                self.paddle.y = self.paddle_area_lower
            else:
                self.paddle.y = mouse.y - self.paddle.height / 2
        
        if mouse.x + self.paddle.width / 2 > self.window.width:  # right boundary
            self.paddle.x = self.window.width - self.paddle.width
        elif mouse.x - self.paddle.width / 2 < 0:  # left boundary
            self.paddle.x = 0
        else:
            self.paddle.x = mouse.x - self.paddle.width / 2
    
    def set_ball_speed(self, event):
        """
        Give a random speed to ball when clicked
        """
        obj = self.window.get_object_at(event.x, event.y)
        if obj is self.double_ball:
            self.add_ball2()
        elif obj is self.longer_paddle:
            self.add_paddle_width()
        elif obj is self.shorten_paddle:
            self.decrease_paddle_width()
        elif obj is self.free_paddle:
            self.freeing_paddle()
        elif self.__ball_dx == 0 and self.__ball_dy == 0:  # do nothing if ball is moving
            self.__ball_dx = random.randint(1, MAX_X_SPEED)
            self.__ball_dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__ball_dx = -self.__ball_dx
    
    def add_ball2(self, ball_radius=BALL_RADIUS):
        self.ball2 = GOval(ball_radius * 2, ball_radius * 2)
        self.ball2.filled = True
        self.ball2.fill_color = 'purple'
        self.window.add(self.ball2, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)
        self.__ball2_dx = random.randint(1, MAX_X_SPEED)
        self.__ball2_dy = random.randint(4, INITIAL_Y_SPEED)
        if random.random() > 0.5:
            self.__ball2_dx = -self.__ball2_dx
    
    def add_paddle_width(self, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                         paddle_offset=PADDLE_OFFSET):
        old_paddle_x = self.paddle.x
        old_paddle_width = self.paddle.width
        self.window.remove(self.paddle)
        self.paddle = GRect(old_paddle_width + 5, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=old_paddle_x,
                        y=self.window.height - paddle_offset - self.status_board_height)
        self.is_long_paddle = True
    
    def freeing_paddle(self):
        self.is_free_paddle = True
    
    def decrease_paddle_width(self, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                              paddle_offset=PADDLE_OFFSET):
        old_paddle_x = self.paddle.x
        old_paddle_width = self.paddle.width
        self.window.remove(self.paddle)
        self.paddle = GRect(old_paddle_width - 5, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=old_paddle_x,
                        y=self.window.height - paddle_offset - self.status_board_height)
        self.is_long_paddle = True
    
    def reset_paddle_width(self, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                           paddle_offset=PADDLE_OFFSET):
        old_paddle_x = self.paddle.x
        self.window.remove(self.paddle)
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=old_paddle_x,
                        y=self.window.height - paddle_offset - self.status_board_height)
        self.is_long_paddle = False
    
    def check_game_ball1(self):
        ball_x = self.ball.x
        ball_y = self.ball.y
        ball_r = self.ball.width / 2
        check1 = self.window.get_object_at(ball_x, ball_y)  # upper left
        check2 = self.window.get_object_at(ball_x + ball_r * 2, ball_y)  # upper right
        check3 = self.window.get_object_at(ball_x, ball_y + ball_r * 2)  # lower left
        check4 = self.window.get_object_at(ball_x + ball_r * 2, ball_y + ball_r * 2)  # lower right
        if check1 is not None:
            if check1 is self.paddle:
                if self.is_long_paddle:
                    self.long_paddle_time -= 1
                self.__ball_dy = -abs(self.__ball_dy)
            elif check1 is self.status_board:
                pass
            elif check1 is self.score_board:
                pass
            elif check1 is self.life_board:
                pass
            elif check1 is self.ball2:
                pass
            else:
                self.update_brick(check1)
                self.add_score()
                self.__ball_dy *= -1
        elif check2 is not None:
            if check2 is self.paddle:
                if self.is_long_paddle:
                    self.long_paddle_time -= 1
                self.__ball_dy = -abs(self.__ball_dy)
            elif check2 is self.status_board or check2 is self.score_board:
                pass
            elif check2 is self.life_board or check2 is self.ball2:
                pass
            else:
                self.update_brick(check2)
                self.add_score()
                self.__ball_dy *= -1
        elif check3 is not None:
            if check3 is self.paddle:
                if self.is_long_paddle:
                    self.long_paddle_time -= 1
                self.__ball_dy = -abs(self.__ball_dy)
            elif check3 is self.status_board:
                pass
            elif check3 is self.score_board:
                pass
            elif check3 is self.life_board:
                pass
            elif check3 is self.ball2:
                pass
            else:
                self.update_brick(check3)
                self.add_score()
                self.__ball_dy *= -1
        elif check4 is not None:
            if check4 is self.paddle:
                if self.is_long_paddle:
                    self.long_paddle_time -= 1
                self.__ball_dy = -abs(self.__ball_dy)
            elif check4 is self.status_board:
                pass
            elif check4 is self.score_board:
                pass
            elif check4 is self.life_board:
                pass
            elif check4 is self.ball2:
                pass
            else:
                self.update_brick(check4)
                self.add_score()
                self.__ball_dy *= -1
        
        #  check if hit the wall
        if self.ball.x + self.ball.width >= self.window.width or self.ball.x <= 0:
            self.__ball_dx *= -1
        if self.ball.y <= 0:
            self.__ball_dy *= -1

    def check_game_ball2(self):
        ball2_x = self.ball2.x
        ball2_y = self.ball2.y
        ball2_r = self.ball2.width / 2
        check1 = self.window.get_object_at(ball2_x, ball2_y)  # upper left
        check2 = self.window.get_object_at(ball2_x + ball2_r * 2, ball2_y)  # upper right
        check3 = self.window.get_object_at(ball2_x, ball2_y + ball2_r * 2)  # lower left
        check4 = self.window.get_object_at(ball2_x + ball2_r * 2, ball2_y + ball2_r * 2)  # lower right
        if check1 is not None:
            if check1 is self.paddle:
                if self.is_long_paddle:
                    self.long_paddle_time -= 1
                self.__ball2_dy = -abs(self.__ball2_dy)
            elif check1 is self.status_board:
                pass
            elif check1 is self.score_board:
                pass
            elif check1 is self.life_board:
                pass
            elif check1 is self.ball:
                pass
            else:
                self.update_brick(check1)
                self.add_score()
                self.__ball2_dy *= -1
        elif check2 is not None:
            if check2 is self.paddle:
                if self.is_long_paddle:
                    self.long_paddle_time -= 1
                self.__ball2_dy = -abs(self.__ball2_dy)
            elif check2 is self.status_board or check2 is self.score_board:
                pass
            elif check2 is self.life_board or check2 is self.ball:
                pass
            else:
                self.update_brick(check2)
                self.add_score()
                self.__ball2_dy *= -1
        elif check3 is not None:
            if check3 is self.paddle:
                if self.is_long_paddle:
                    self.long_paddle_time -= 1
                self.__ball2_dy = -abs(self.__ball2_dy)
            elif check3 is self.status_board:
                pass
            elif check3 is self.score_board:
                pass
            elif check3 is self.life_board:
                pass
            elif check3 is self.ball:
                pass
            else:
                self.update_brick(check3)
                self.add_score()
                self.__ball2_dy *= -1
        elif check4 is not None:
            if check4 is self.paddle:
                if self.is_long_paddle:
                    self.long_paddle_time -= 1
                self.__ball2_dy = -abs(self.__ball2_dy)
            elif check4 is self.status_board:
                pass
            elif check4 is self.score_board:
                pass
            elif check4 is self.life_board:
                pass
            elif check4 is self.ball:
                pass
            else:
                self.update_brick(check4)
                self.add_score()
                self.__ball2_dy *= -1
    
        #  check if hit the wall
        if self.ball2.x + self.ball2.width >= self.window.width or self.ball2.x <= 0:
            self.__ball2_dx *= -1
        if self.ball2.y <= 0:
            self.__ball2_dy *= -1

    def unfree_paddle(self):
        self.paddle.y = self.paddle_area_lower
        self.is_free_paddle = False
    
    def check_drop_out1(self):
        """
        check if dropped out of window
        :return: "drop out", when the ball drops out of window, for user to decrease the lives
        """
        if self.ball.y >= self.window.height - self.status_board.height:
            self.reset_ball()
            self.life -= 1
            self.life_board.text = " "*4*(3-self.life) + chr(10084)*self.life
            return True
    
    def check_drop_out2(self):
        """
        check if dropped out of window
        :return: "drop out", when the ball drops out of window, for user to decrease the lives
        """
        if self.ball2.y >= self.window.height - self.status_board.height:
            self.window.remove(self.ball2)
    
    def reset_ball(self):
        """
        reset ball to the initial position and with 0 speed
        """
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        self.__ball_dx = 0
        self.__ball_dy = 0
        self.unfree_paddle()
        self.reset_paddle_width()
    
    def get_ball_speed_x(self):
        return self.__ball_dx
    
    def get_ball_speed_y(self):
        return self.__ball_dy
    
    def get_ball2_speed_x(self):
        return self.__ball2_dx
    
    def get_ball2_speed_y(self):
        return self.__ball2_dy
    
    def get_brick_amount(self):
        return self.__brick_amount
    
    def add_score(self):
        self.score += 1
        self.score_board.text = f"Score: {self.score}"
