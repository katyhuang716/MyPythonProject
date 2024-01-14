"""
File: 
Name:Hsinhuihuang
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Constants
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Initialize window
window = GWindow(800, 500, title='bouncing_ball.py')

# Create a ball
ball = GOval(SIZE, SIZE)
ball.filled = True
ball.color = 'black'
ball.fill_color = 'black'

# Add ball to the window
window.add(ball, x=START_X, y=START_Y)

# Initial ball velocity
vy = 0
# Number of times the ball has been clicked to start falling
click_count = 0
# Whether the ball is currently moving
is_moving = False


def main():
    # Register event handlers
    onmouseclicked(handle_click)


def handle_click(event):
    global click_count, is_moving
    # Start the ball's movement only if it's not already moving
    if not is_moving:
        click_count += 1
        is_moving = True
        animate_ball()


def animate_ball():
    global vy, is_moving, click_count
    # Animate the ball until it has been clicked to start three times
    while click_count <= 3:
        # Move the ball
        ball.move(VX, vy)
        # Update the vertical velocity
        vy += GRAVITY
        # If the ball touches the ground, bounce it
        if ball.y + SIZE >= window.height:
            vy = -vy * REDUCE
        # If the ball goes beyond the right edge, reset it
        if ball.x > window.width:
            window.add(ball, START_X, START_Y)
            vy = 0
            is_moving = False
            break
        # Pause for the next frame
        pause(DELAY)
    # Stop the ball after the third click
    if click_count > 3:
        is_moving = False


if __name__ == "__main__":
    main()

