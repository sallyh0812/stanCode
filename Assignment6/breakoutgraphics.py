"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Name: Sally 111613025
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        """
        Make the initial window with some bricks, a ball, a paddle, and start the mouse listener
        """
        
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width - self.paddle.width) / 2,
                        y=self.window.height - paddle_offset)
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
        self.brick_color = 'red'
        for i in range(brick_rows):
            current_x = 0
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = self.brick_color
                self.window.add(self.brick, x=current_x, y=current_y)
                current_x += self.brick.width + brick_spacing
            current_y += self.brick.height + brick_spacing
            if i % 2 == 1:
                #  change bricks' color every 2 rows
                self.change_brick_color()
        
        # Default initial bricks amount
        self.__brick_amount = brick_cols * brick_rows
        
        # Initialize our mouse listeners
        onmouseclicked(self.set_ball_speed)
        onmousemoved(self.move_paddle)
    
    def change_brick_color(self):
        """
        Change the bricks' color according to the current brick color when adding bricks to the window
        """
        if self.brick_color == 'red':
            self.brick_color = 'orange'
        elif self.brick_color == 'orange':
            self.brick_color = 'yellow'
        elif self.brick_color == 'yellow':
            self.brick_color = 'green'
        elif self.brick_color == 'green':
            self.brick_color = 'blue'
        elif self.brick_color == 'blue':
            self.brick_color = 'red'
    
    def move_paddle(self, mouse):
        """
        Set paddle.x to current mouse.x
        """
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
        if self.__ball_dx == 0 and self.__ball_dy == 0:  # do nothing if ball is moving
            self.__ball_dx = random.randint(1, MAX_X_SPEED)
            self.__ball_dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__ball_dx = -self.__ball_dx
    
    def check_collision(self):
        """
        Check if the ball hit the paddle, the bricks, the walls.
        Hit the paddle: bounce up
        Hit the bricks: remove the brick and bounce
        Hit the walls: bounce
        Bounce by changing the direction of speed (__ball_dx or __ball_dy)
        
        """
        ball_x = self.ball.x
        ball_y = self.ball.y
        ball_r = self.ball.width / 2
        check1 = self.window.get_object_at(ball_x, ball_y)  # upper left
        check2 = self.window.get_object_at(ball_x + ball_r * 2, ball_y)  # upper right
        check3 = self.window.get_object_at(ball_x, ball_y + ball_r * 2)  # lower left
        check4 = self.window.get_object_at(ball_x + ball_r * 2, ball_y + ball_r * 2)  # lower right
        if check1 is not None:
            if check1 is not self.paddle:  # if hit the brick
                self.window.remove(check1)
                self.__brick_amount -= 1
                self.__ball_dy *= -1
            else:  # if hit the paddle
                # make sure it goes up even when it hits the paddle from the side
                self.__ball_dy = -abs(self.__ball_dy)
        elif check2 is not None:
            if check2 is not self.paddle:
                self.window.remove(check2)
                self.__brick_amount -= 1
                self.__ball_dy *= -1
            else:
                self.__ball_dy = -abs(self.__ball_dy)
        elif check3 is not None:
            if check3 is not self.paddle:
                self.window.remove(check3)
                self.__brick_amount -= 1
                self.__ball_dy *= -1
            else:
                self.__ball_dy = -abs(self.__ball_dy)
        elif check4 is not None:
            if check4 is not self.paddle:
                self.window.remove(check4)
                self.__brick_amount -= 1
                self.__ball_dy *= -1
            else:
                self.__ball_dy = -abs(self.__ball_dy)
        
        #  check if hit the wall
        if self.ball.x + self.ball.width >= self.window.width or self.ball.x <= 0:
            self.__ball_dx *= -1
        if self.ball.y <= 0:
            self.__ball_dy *= -1
            
    def check_drop_out(self):
        """
        check if dropped out of window
        :return: "drop out", when the ball drops out of window, for user to decrease the lives
        """
        if self.ball.y >= self.window.height:
            self.reset_ball()
            return True
    
    def reset_ball(self):
        """
        reset ball to the initial position and with 0 speed
        """
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        self.__ball_dx = 0
        self.__ball_dy = 0
    
    def get_ball_speed_x(self):
        return self.__ball_dx
    
    def get_ball_speed_y(self):
        return self.__ball_dy
    
    def get_brick_amount(self):
        return self.__brick_amount
