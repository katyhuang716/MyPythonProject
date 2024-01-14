"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts
first_v = False
graphics = BreakoutGraphics()
dy = graphics.get_dy()
dx = graphics.get_dx()
lives = NUM_LIVES


def main():
    global lives  # Declare 'lives' as a global variable

    while lives > 0:  # Continue the game while the player still has lives
        # If the game has started, move the ball
        if graphics.is_game_started:
            ball_out = graphics.move_ball()  # Move the ball and check if it falls out
            if ball_out:  # If the ball falls out of the window
                lives -= 1  # Decrease the number of lives
                graphics.is_game_started = False  # Wait for the next click to restart

        # Pause for a short duration to control the frame rate
        pause(FRAME_RATE)

        # Check if all bricks have been removed
        if graphics.brick_count == 0:  # If the count of bricks is zero
            break  # End the game loop


if __name__ == '__main__':
    main()  # Start the game by calling the main function

