"""
File: draw_line.py
Name: Sally 111613025
-------------------------
A program that enables user to draw lines by clicking start and end points
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10

# initialize circle and window
circle = GOval(SIZE, SIZE)
window = GWindow()

# global variable, show if there is circle in window
is_circle = False


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(event):
    """
    :param event: event.x, event.y shows the position user clicked on
    Add circle if it's the first click.
    Draw a line and remove the circle if it's a second click.
    """
    global is_circle
    
    if is_circle:  # if this is a second click
        line = GLine(circle.x + circle.width / 2, circle.y + circle.height / 2, event.x, event.y)
        window.remove(circle)  # remove the start point circle
        window.add(line)
        is_circle = False
        
    else:  # if this is the first click
        window.add(circle, x=event.x - circle.width / 2, y=event.y - circle.height / 2)
        is_circle = True


if __name__ == "__main__":
    main()
