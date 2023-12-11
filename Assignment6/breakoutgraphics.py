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
BRICK_ROWS = 7  # Number of rows of bricks
BRICK_COLS = 5  # Number of columns of bricks
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
        self.ball.__dx = 0
        self.ball.__dy = 0
        
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
                self.change_brick_color()
        
        # Initialize our mouse listeners
        onmouseclicked(self.set_ball_speed)
        onmousemoved(self.move_paddle)
        
        ##
        self.brick_amount = brick_cols * brick_rows
    
    def change_brick_color(self):
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
        if mouse.x + self.paddle.width / 2 > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        elif mouse.x - self.paddle.width / 2 < 0:
            self.paddle.x = 0
        else:
            self.paddle.x = mouse.x - self.paddle.width / 2
    
    def set_ball_speed(self, event):
        if self.ball.__dx == 0 and self.ball.__dy == 0:
            self.ball.__dx = random.randint(1, MAX_X_SPEED)
            self.ball.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.ball.__dx = -self.ball.__dx
    
    def get_ball_speed_x(self):
        return self.ball.__dx
    
    def get_ball_speed_y(self):
        return self.ball.__dy
    
    def check_collision(self):
        x = self.ball.x
        y = self.ball.y
        r = self.ball.width / 2
        check1 = self.window.get_object_at(x, y)
        check2 = self.window.get_object_at(x + r * 2, y)
        check3 = self.window.get_object_at(x, y + r * 2)
        check4 = self.window.get_object_at(x + r * 2, y + r * 2)
        if check1 is not None:
            if check1 is not self.paddle:
                self.window.remove(check1)
                self.brick_amount -= 1
            self.ball.__dy *= -1
        elif check2 is not None:
            if check2 is not self.paddle:
                self.window.remove(check2)
                self.brick_amount -= 1
            self.ball.__dy *= -1
        elif check3 is not None:
            if check3 is not self.paddle:
                self.window.remove(check3)
                self.brick_amount -= 1
            self.ball.__dy *= -1
        elif check4 is not None:
            if check4 is not self.paddle:
                self.window.remove(check4)
                self.brick_amount -= 1
            self.ball.__dy *= -1
        
        if self.ball.y > self.window.height:
            self.reset_ball()
            return "drop out"
        
        if self.ball.x + self.ball.width >= self.window.width or self.ball.x <= 0:
            self.ball.__dx *= -1
        if self.ball.y <= 0:
            self.ball.__dy *= -1
    
    def reset_ball(self):
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        self.ball.__dx = 0
        self.ball.__dy = 0
