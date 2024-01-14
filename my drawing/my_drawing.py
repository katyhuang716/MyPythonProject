"""
File: 
Name: Hsinhuihuang
Christmas is undoubtedly my favorite time of the year. The scene I am creating features a beautifully decorated Christmas tree, embellished with a range of ornaments, and surrounded by gifts. This visual tableau is a reflection of the joy and warmth that Christmas brings to me.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GRect, GPolygon, GOval, GLabel
import random


def main():
    window = GWindow(width=800, height=500, title='Christmas Tree')

    # Draw the Christmas tree
    draw_christmas_tree(window)

    # Add decorations
    add_decorations(window)

    # Add 'Merry Christmas' text
    add_merry_christmas_label(window)

    # Add 'stanCode101' text
    add_stanCode101_label(window)

    draw_sleigh(window)

    draw_gift_boxes(window)

    draw_snowman(window, 700, 350)  # Adjust x, y coordinates as needed

    draw_snowman_details

    # Add snowflakes
    for _ in range(100):  # Number of snowflakes
        x = random.randint(0, 800)
        y = random.randint(0, 500)
        snowflake = GOval(5, 5, x=x, y=y)
        snowflake.filled = True
        snowflake.fill_color = random.choice(['white', 'snow'])
        window.add(snowflake)


def draw_christmas_tree(window):
    # Drawing the tree
    tree_height = [120, 100, 80]  # Height of the tree
    tree_width = [200, 150, 100]  # Width of the tree
    y = 300  # Initial y-coordinate

    for i in range(len(tree_height)):
        tree_layer = GPolygon()
        tree_layer.add_vertex((400 - tree_width[i] / 2, y))
        tree_layer.add_vertex((400, y - tree_height[i]))
        tree_layer.add_vertex((400 + tree_width[i] / 2, y))
        tree_layer.filled = True
        tree_layer.fill_color = 'green'
        window.add(tree_layer)
        y -= tree_height[i] - 20  # Starting height for the next layer

    # Drawing the tree trunk
    trunk = GRect(30, 50, x=385, y=300)
    trunk.filled = True
    trunk.fill_color = 'brown'
    window.add(trunk)


def add_decorations(window):
    # Randomly adding decorations
    for _ in range(40):  # Number of decorations
        x = random.randint(200, 550)
        y = random.randint(100, 330)
        decoration = GOval(10, 10, x=x, y=y)
        decoration.filled = True
        decoration.fill_color = random.choice(['red', 'yellow', 'pink', 'blue', 'silver', 'gold'])
        window.add(decoration)

    # Adding a star
    star = GLabel('✶', x=382, y=50)
    star.font = 'SansSerif-50'
    star.color = 'gold'
    window.add(star)


def add_merry_christmas_label(window):
    label = GLabel('Merry Christmas', x=20, y=40)  # Position of the label in the window
    label.font = 'Times-24-bold'  # Setting the font and size
    label.color = 'red'  # Setting the color
    window.add(label)


def add_stanCode101_label(window):
    label = GLabel('stanCode101', x=325, y=90)  # Position of the label in the window
    label.font = 'Times-20-bold'  # Setting the font and size
    label.color = 'tomato'  # Setting the color
    window.add(label)


def draw_sleigh(window):
    # Draw the main body of the sleigh
    sleigh_body = GPolygon()
    sleigh_body.add_vertex((650, 400))
    sleigh_body.add_vertex((750, 400))
    sleigh_body.add_vertex((730, 450))
    sleigh_body.add_vertex((670, 450))
    sleigh_body.filled = True
    sleigh_body.fill_color = 'red'
    sleigh_body.color = 'black'
    window.add(sleigh_body)

    # Draw the front part of the sleigh
    sleigh_front = GPolygon()
    sleigh_front.add_vertex((750, 400))
    sleigh_front.add_vertex((770, 430))
    sleigh_front.add_vertex((730, 450))
    sleigh_front.filled = True
    sleigh_front.fill_color = 'red'
    sleigh_front.color = 'black'
    window.add(sleigh_front)

    # Add decoration to the sleigh
    decoration = GOval(10, 10, x=710, y=420)
    decoration.filled = True
    decoration.fill_color = 'yellow'
    window.add(decoration)


def draw_gift_boxes(window):
    # First gift box
    draw_gift_box(window, 320, 330, 50, 50, 'blue', 'yellow')

    # Second gift box
    draw_gift_box(window, 480, 350, 60, 40, 'red', 'green')

    # Third gift box
    draw_gift_box(window, 250, 320, 40, 60, 'purple', 'gold')

    # Fourth gift box
    draw_gift_box(window, 420, 330, 45, 45, 'pink', 'silver')

    # Fifth gift box
    draw_gift_box(window, 550, 310, 45, 45, 'gold', 'silver')


def draw_gift_box(window, x, y, width, height, fill_color, ribbon_color):
    # Main body of the gift box
    gift_box = GRect(width, height, x=x, y=y)
    gift_box.filled = True
    gift_box.fill_color = fill_color
    window.add(gift_box)

    # Ribbons
    # Horizontal
    ribbon1 = GRect(width, 5, x=x, y=y + height / 2 - 2.5)
    ribbon1.filled = True
    ribbon1.fill_color = ribbon_color
    window.add(ribbon1)
    # Vertical
    ribbon2 = GRect(5, height, x=x + width / 2 - 2.5, y=y)
    ribbon2.filled = True
    ribbon2.fill_color = ribbon_color
    window.add(ribbon2)


def draw_snowman(window, x, y):
    # # Draw bottom circle
    # bottom_circle = GOval(40, 40, x=x, y=y)
    # bottom_circle.filled = True
    # bottom_circle.fill_color = 'white'
    # window.add(bottom_circle)

    # Draw middle circle
    middle_circle = GOval(50, 50, x=x, y=y)
    middle_circle.filled = True
    middle_circle.fill_color = 'white'
    window.add(middle_circle)

    # Draw top circle (head)
    top_circle = GOval(30, 30, x=x + 10, y=y - 30)
    top_circle.filled = True
    top_circle.fill_color = 'white'
    window.add(top_circle)

    # Draw eyes, nose, and buttons
    # Adjust coordinates as needed for the details
    draw_snowman_details(window, x + 10, y - 30)


def draw_snowman_details(window, x, y):
    # Draw eyes
    eye_offset = 5  # Increase this value to move the eyes further to the right

    # Draw left eye
    left_eye = GOval(5, 5, x=x + 3 + eye_offset, y=y + 5)
    left_eye.filled = True
    left_eye.fill_color = 'black'
    window.add(left_eye)

    # Draw right eye
    right_eye = GOval(5, 5, x=x + 12 + eye_offset, y=y + 5)
    right_eye.filled = True
    right_eye.fill_color = 'black'
    window.add(right_eye)

    # Draw carrot nose
    nose_offset = 3  # Increase this value to move the nose further to the right

    nose = GPolygon()
    nose.add_vertex((x + 11 + nose_offset, y + 12))
    nose.add_vertex((x + 21 + nose_offset, y + 14))
    nose.add_vertex((x + 11 + nose_offset, y + 17))
    nose.filled = True
    nose.fill_color = 'orange'
    window.add(nose)

    # Draw buttons

    button_vertical_offset = -5  # Decrease this value to move the buttons further up

    for i in range(3):
        button = GOval(5, 5, x=x + 13, y=y + 39 + (i * 15))
        button.filled = True
        button.fill_color = 'black'
        window.add(button)


if __name__ == '__main__':
    main()

