"""Group 2 Final Project
Michael Newman, Alexandria Zitting, Danh Doan
Modified version of freegames TicTacToe:
https://grantjenks.com/docs/freegames/tictactoe.html
"""

#import turtle for turtle graphics

from turtle import *

#import line from freegames to draw a line for the board

from freegames import line

#draw 4 lines to form the grid, 100 pixels apart horizontally and vertically
#at the end we define the coordinates. top left = 0,0. Bottom right = 300,300

def grid():
    """Draw tic-tac-toe grid."""
    #Vertical lines (at x = 100, 200)
    #(starting x, starting y, ending x, ending y)
    line(100, 0, 100, 300)   # First vertical line
    line(200, 0, 200, 300)   # Second vertical line

    #Horizontal lines (at y = 100, 200)
    #(starting x, starting y, ending x, ending y)
    line(0, 100, 300, 100)   # First horizontal line
    line(0, 200, 300, 200)   # Second horizontal line


#we updated the old function here to use fit our 100x100px squares and color it blue
#we are drawing the x, giving 10px of buffer room inside our 100x100px squares

def drawx(x, y):
    """Draw X player inside 100x100 cell."""
    color('blue')
    line(x + 10, y + 10, x + 90, y + 90)
    line(x + 10, y + 90, x + 90, y + 10)

#we updated the old function to draw red o's inside of the 100x100px squares

def drawo(x, y):
    """Draw O player inside 100x100 cell."""
    up()
    color('red')
    goto(x + 50, y + 10)
    down()
    circle(40)


#we use this to define where on the floor(grid) we draw our x and o's
#it gives us a consistent spot on the grid so they are centered consistently

def floor(value):
    """Snap to nearest 100 unit grid."""
    return (value // 100) * 100

#track who's turn it is

state = {'player': 0}
players = [drawx, drawo]

#handle when a player taps the screen. listen for the location, pass the x/y values to our floor() function
#floor() gives us a consistent spot on the board where we draw an x or o depending on who's turn it is
#then we update the screen and change who's turn it is

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

#hide the turtle so we don't see him drawing

hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
