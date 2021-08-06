from cmu_112_graphics import *
from pacman import Pacman
from ghost import *

def appStarted(app):
    app.background = app.  scaleImage(app.loadImage(
        'SpriteSheet.png').crop((370, 3, 536, 216)), 3.5)
    app.dot = app.scaleImage(app.loadImage(
        'SpriteSheet.png').crop((3, 81, 5, 83)), 3.5)
    app.blank = app.scaleImage(app.loadImage(
        'SpriteSheet.png').crop((5, 81, 7, 83)), 3.5)
    app.pacman = Pacman(app, (21, 11))
    app.pacmanImg = app.pacman.getImg()
    app.ghost = basicGhost(app, (10, 10))
    app.ghostImg = app.ghost.getImg()
    app.timerDelay = 20

    app.board = [["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                 ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X"],
                 ["X", " ", "X", "X", "X", " ", "X", "X", "X", " ", "X", " ", "X", "X", "X", " ", "X", "X", "X", " ", "X"],
                 ["X", " ", "X", "X", "X", " ", "X", "X", "X", " ", "X", " ", "X", "X", "X", " ", "X", "X", "X", " ", "X"],
                 ["X", " ", "X", "X", "X", " ", "X", "X", "X", " ", "X", " ", "X", "X", "X", " ", "X", "X", "X", " ", "X"],
                 ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X"],
                 ["X", " ", "X", "X", "X", " ", "X", " ", "X", "X", "X", "X", "X", " ", "X", " ", "X", "X", "X", " ", "X"],
                 ["X", " ", "X", "X", "X", " ", "X", " ", "X", "X", "X", "X", "X", " ", "X", " ", "X", "X", "X", " ", "X"],
                 ["X", " ", " ", " ", " ", " ", "X", " ", " ", " ", "X", " ", " ", " ", "X", " ", " ", " ", " ", " ", "X"],
                 ["X", "X", "X", "X", "X", " ", "X", "X", "X", "O", "X", "O", "X", "X", "X", " ", "X", "X", "X", "X", "X"],
                 ["X", "X", "X", "X", "X", " ", "X", "O", "O", "O", "O", "O", "O", "O", "X", " ", "X", "X", "X", "X", "X"],
                 ["X", "X", "X", "X", "X", " ", "X", "O", "X", "X", "X", "X", "X", "O", "X", " ", "X", "X", "X", "X", "X"],
                 ["X", "X", "X", "X", "X", " ", "X", "O", "X", "X", "X", "X", "X", "O", "X", " ", "X", "X", "X", "X", "X"],
                 ["O", "O", "O", "O", "O", " ", "O", "O", "X", "X", "X", "X", "X", "O", "O", " ", "O", "O", "O", "O", "O"],
                 ["X", "X", "X", "X", "X", " ", "X", "O", "X", "X", "X", "X", "X", "O", "X", " ", "X", "X", "X", "X", "X"],
                 ["X", "X", "X", "X", "X", " ", "X", "O", "O", "O", "O", "O", "O", "O", "X", " ", "X", "X", "X", "X", "X"],
                 ["X", "X", "X", "X", "X", " ", "X", "O", "X", "X", "X", "X", "X", "O", "X", " ", "X", "X", "X", "X", "X"],
                 ["X", "X", "X", "X", "X", " ", "X", " ", "X", "X", "X", "X", "X", " ", "X", " ", "X", "X", "X", "X", "X"],
                 ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X"],
                 ["X", " ", "X", "X", "X", " ", "X", "X", "X", " ", "X", " ", "X", "X", "X", " ", "X", "X", "X", " ", "X"],
                 ["X", " ", " ", " ", "X", " ", " ", " ", " ", " ", "O", " ", " ", " ", " ", " ", "X", " ", " ", " ", "X"],
                 ["X", "X", "X", " ", "X", " ", "X", " ", "X", "X", "X", "X", "X", " ", "X", " ", "X", " ", "X", "X", "X"],
                 ["X", "X", "X", " ", "X", " ", "X", " ", "X", "X", "X", "X", "X", " ", "X", " ", "X", " ", "X", "X", "X"],
                 ["X", " ", " ", " ", " ", " ", "X", " ", " ", " ", "X", " ", " ", " ", "X", " ", " ", " ", " ", " ", "X"],
                 ["X", " ", "X", "X", "X", "X", "X", "X", "X", " ", "X", " ", "X", "X", "X", "X", "X", "X", "X", " ", "X"],
                 ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X"],
                 ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ]
def keyPressed(app, event):
    if (event.key == "Up"):
        app.pacman.changeDir(2)
    elif (event.key == "Down"):
        app.pacman.changeDir(3)
    elif (event.key == "Left"):
        app.pacman.changeDir(1)
    elif (event.key == "Right"):
        app.pacman.changeDir(0)  


def timerFired(app):
    app.pacmanImg = app.pacman.getImg()
    app.ghostImg = app.ghost.getImg()
    app.ghost.nextSprite()
    #app.pacman.nextSprite()
    app.pacman.move()
    app.board[app.pacman.pos[0]][app.pacman.pos[1]] = "O"
    app.ghost.move()

def getCenter(app, pos):
    cellWidth = app.width/21
    return ((pos[1]-0.5) * cellWidth, (pos[0] - 0.5) * cellWidth)

def redrawAll(app, canvas):
    canvas.create_image(
        0, 0, image=ImageTk.PhotoImage(app.background), anchor="nw")
    drawDots(app, canvas)

    #drawPacman
    x,y = app.pacman.center
    canvas.create_image(x, y, image = ImageTk.PhotoImage(app.pacmanImg), anchor = "c")
    x,y = app.ghost.center
    canvas.create_image(x, y, image = ImageTk.PhotoImage(app.ghostImg), anchor = "c")
   
def drawDots(app, canvas):
    for row in range(len(app.board)):
        for col in range(len(app.board[row])):
            if (app.board[row][col] == " "):
                canvas.create_image(
                    7 + (28 * col), 7 + (28 * row), image=ImageTk.PhotoImage(app.dot), anchor="nw")
            elif (app.board[row][col] == "O"):
                canvas.create_image(
                    7 + (28 * col), 7 + (28 * row), image=ImageTk.PhotoImage(app.blank), anchor="nw")
                

runApp(width=579, height=747)
