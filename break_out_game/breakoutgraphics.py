"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Initialize paddle and ball movement
        self.__dx = 0
        self.__dy = 0
        self.is_game_started = False
        self.brick_count = BRICK_ROWS * BRICK_COLS  # 初始化磚塊計數器

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        # Center a filled ball in the graphical window
        # Default initial velocity for the ball
        # Initialize our mouse listeners
        # Draw bricks

        # Create the paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.color = 'black'  # You can choose any color you like
        self.paddle.fill_color = 'black'
        # Set the initial position of the paddle
        paddle_x = (self.window.width - paddle_width) / 2
        paddle_y = self.window.height - paddle_height - paddle_offset
        self.window.add(self.paddle, x=paddle_x, y=paddle_y)

        # Set the initial position of the paddle
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.ball.color = 'black'  # Again, you can set the color to your preference
        self.ball.fill_color = 'black'
        # 設置球的初始位置
        ball_x = (self.window.width - ball_radius * 2) / 2
        ball_y = (self.window.height - ball_radius * 2) / 2
        self.window.add(self.ball, x=ball_x, y=ball_y)

        # Define colors for each row of bricks
        brick_colors = ["red", "orange", "yellow", "green", "blue"]

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                # Change the color every two rows according to the brick_colors list
                color_index = i // 2 % len(brick_colors)  # Use integer division and modulo to cycle color indices
                brick.fill_color = brick_colors[color_index]
                brick.color = brick_colors[color_index]
                # Set the position of the brick
                brick_x = j * (brick_width + brick_spacing)
                brick_y = brick_offset + i * (brick_height + brick_spacing)
                self.window.add(brick, x=brick_x, y=brick_y)

        # Initialize mouse listeners
        onmouseclicked(self.handle_mouse_click)
        onmousemoved(self.handle_mouse_move)

    def handle_mouse_click(self, event):
        # Implement the initial velocity and action of the ball here
        if not self.is_game_started:
            self.is_game_started = True
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def handle_mouse_move(self, event):
        # Make the paddle center follow the mouse's x-coordinate but do not let it go beyond the window's sides
        # This ensures that the paddle is always fully visible in the window
        paddle_x = event.x - self.paddle.width / 2
        if paddle_x < 0:
            paddle_x = 0
        elif paddle_x > self.window.width - self.paddle.width:
            paddle_x = self.window.width - self.paddle.width
        self.paddle.x = paddle_x

    # To access the speed outside of the class, add getter methods
    def get_dx(self):
        # Return the private variable for horizontal velocity
        return self.__dx

    def get_dy(self):
        # Return the private variable for vertical velocity
        return self.__dy

    # def move_ball(self):
    #     """移動球並處理碰撞。"""
    #     self.ball.move(self.__dx, self.__dy)
    #
    #     # 檢查並處理邊界碰撞
    #     if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
    #         self.__dx = -self.__dx
    #     if self.ball.y <= 0:
    #         self.__dy = -self.__dy
    #
    #     # 檢查其他碰撞
    #     self.check_for_collision()

    def move_ball(self):
        """Move the ball and handle collisions."""
        self.ball.move(self.__dx, self.__dy)

        # Check and handle boundary collisions
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy

        # Check for other collisions
        self.check_for_collision()

        # Check if the ball falls below the bottom edge
        if self.ball.y > self.window.height:
            self.reset_ball_position()
            return True  # Signal that the ball has fallen out
        return False

    def check_for_collision(self):
        """
        Checks for collision at the ball's corners and handles the collision accordingly.
        """
        # Getting the radius for use in the corners calculation
        r = BALL_RADIUS

        # Checking each corner for a collision
        for i in range(4):
            # Assign corner based on index
            if i == 0:  # Top-left corner
                corner_x = self.ball.x
                corner_y = self.ball.y
            elif i == 1:  # Top-right corner
                corner_x = self.ball.x + 2 * r
                corner_y = self.ball.y
            elif i == 2:  # Bottom-left corner
                corner_x = self.ball.x
                corner_y = self.ball.y + 2 * r
            elif i == 3:  # Bottom-right corner
                corner_x = self.ball.x + 2 * r
                corner_y = self.ball.y + 2 * r

            collision_obj = self.window.get_object_at(corner_x, corner_y)
            if collision_obj:
                # If the ball hits the paddle, bounce up
                if collision_obj == self.paddle:
                    self.__dy = -abs(self.__dy)  # Ensure the ball always bounces up
                    break  # Only process one collision

                # If the ball hits a brick, remove the brick and bounce
                else:
                    self.window.remove(collision_obj)
                    self.__dy = -self.__dy  # Reverse the y velocity
                    self.brick_count -= 1  # 減少磚塊計數
                    break  # Only process one collision

    def reset_ball_position(self):
        # Resets the ball to the starting position in the center of the window.
        start_x = (self.window.width - self.ball.width) / 2
        start_y = (self.window.height - self.ball.height) / 2
        self.window.add(self.ball, start_x, start_y)
        self.__dx = 0
        self.__dy = 0
        self.is_game_started = False







