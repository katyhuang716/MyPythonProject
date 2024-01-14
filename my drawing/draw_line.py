"""
File: 
Name:Hsinhuihuang
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Constants
SIZE = 6  # This can be set to any size for the circle radius

# Global variables
window = GWindow()
start_point = None
circle = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line_or_circle)


def draw_line_or_circle(mouse):
    global start_point, circle
    if start_point is None:
        # First click - draw circle
        start_point = (mouse.x, mouse.y)
        circle = GOval(SIZE * 2, SIZE * 2)
        circle.x = mouse.x - SIZE
        circle.y = mouse.y - SIZE
        circle.color = "black"
        circle.filled = False
        window.add(circle)
    else:
        # Second click - draw line and remove circle
        end_point = (mouse.x, mouse.y)
        line = GLine(start_point[0], start_point[1], end_point[0], end_point[1])
        window.add(line)
        window.remove(circle)
        # Reset start point for next line
        start_point = None
        circle = None


if __name__ == "__main__":
    main()
