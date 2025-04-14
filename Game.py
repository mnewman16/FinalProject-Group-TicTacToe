from turtle import *

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    # Vertical lines (at x = 100, 200)
    #(starting x, starting y, ending x, ending y)
    line(100, 0, 100, 300)   # First vertical line
    line(200, 0, 200, 300)   # Second vertical line

    # Horizontal lines (at y = 100, 200)
    #(starting x, starting y, ending x, ending y)
    line(0, 100, 300, 100)   # First horizontal line
    line(0, 200, 300, 200)   # Second horizontal line


def drawx(x, y):
    """Draw X player inside 100x100 cell."""
    color('blue')
    line(x + 10, y + 10, x + 90, y + 90)
    line(x + 10, y + 90, x + 90, y + 10)


def drawo(x, y):
    """Draw O player inside 100x100 cell."""
    up()
    color('red')
    goto(x + 50, y + 10)
    down()
    circle(40)


def floor(value):
    """Snap to nearest 100 unit grid."""
    return (value // 100) * 100


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player

#set size of window to 300x300
setup(300, 300)
#set coordinates
#top left is 0,0, top right is 300,0
#bottom right is 300,300, bottom left is 0,300
#this makes the setup fill the screen since I changed the dimmensions to make the math clearer.
setworldcoordinates(0, 300, 300, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
