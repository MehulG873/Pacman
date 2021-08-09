from cmu_112_graphics import *
from pacman import Pacman
from ghost import *
import time


def appStarted(app):
    app.powered = False
    app.board = [["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                 ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X"],
                 ["X", " ", "X", "X", "X", " ", "X", "X", "X", " ", "X", " ", "X", "X", "X", " ", "X", "X", "X", " ", "X"],
                 ["X", "P", "X", "X", "X", " ", "X", "X", "X", " ", "X", " ", "X", "X", "X", " ", "X", "X", "X", "P", "X"],
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
                 ["X", "P", " ", " ", "X", " ", " ", " ", " ", " ", "O", " ", " ", " ", " ", " ", "X", " ", " ", "P", "X"],
                 ["X", "X", "X", " ", "X", " ", "X", " ", "X", "X", "X", "X", "X", " ", "X", " ", "X", " ", "X", "X", "X"],
                 ["X", "X", "X", " ", "X", " ", "X", " ", "X", "X", "X", "X", "X", " ", "X", " ", "X", " ", "X", "X", "X"],
                 ["X", " ", " ", " ", " ", " ", "X", " ", " ", " ", "X", " ", " ", " ", "X", " ", " ", " ", " ", " ", "X"],
                 ["X", " ", "X", "X", "X", "X", "X", "X", "X", " ", "X", " ", "X", "X", "X", "X", "X", "X", "X", " ", "X"],
                 ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X"],
                 ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                 ]
    app.poweredTime = time.time()
    app.background = app.  scaleImage(app.loadImage(
        'SpriteSheet.png').crop((370, 3, 536, 216)), 3.5)
    app.dot = app.scaleImage(app.loadImage(
        'SpriteSheet.png').crop((3, 81, 5, 83)), 3.5)
    app.blank = app.scaleImage(app.loadImage(
        'SpriteSheet.png').crop((5, 81, 7, 83)), 3.5)
    app.pacman = Pacman(app, (20, 10))
    app.pacmanImg = app.pacman.getImg()
    app.title = app.scaleImage(app.loadImage(
        'SpriteSheet.png').crop((2, 4, 184, 50)), 2.75)
    app.ghosts = [dijkstraGhost(app, (10, 10), 0), dijkstraGhost( app, (13, 13), 1), basicGhost(app, (10, 15), 2), basicGhost(app, (7, 13), 3)]
    app.ghostImgs = []
    for ghost in app.ghosts:
        app.ghostImgs.append(ghost.getImg())
    app.timerDelay = 20
    app.score = 0
    

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
    app.pacman.move()
    for i in range(len(app.ghosts)):
        app.ghostImgs[i] = app.ghosts[i].getImg()
        app.ghosts[i].nextSprite()
        app.ghosts[i].move()
        if (app.pacman.pos == app.ghosts[i].pos):
            if app.powered:
                app.ghosts[i].reset()
                app.score += 50
            else:
                time.sleep(10)
    # app.pacman.nextSprite()
    if (app.board[app.pacman.pos[0]][app.pacman.pos[1]] == " "):
        app.score += 1
        app.board[app.pacman.pos[0]][app.pacman.pos[1]] = "O"
    elif (app.board[app.pacman.pos[0]][app.pacman.pos[1]] == "P"):
        app.score += 10
        app.board[app.pacman.pos[0]][app.pacman.pos[1]] = "O"
        app.powered = True
        app.poweredTime = time.time()
    if time.time() > 5 + app.poweredTime:
        app.powered = False


def getCenter(app, pos):
    cellWidth = app.width/21
    return ((pos[1]-0.5) * cellWidth, (pos[0] - 0.5) * cellWidth)


def redrawAll(app, canvas):
    canvas.create_rectangle(-10, -10, app.width + 10,
                            app.height + 10, fill="black")
    canvas.create_image(
        0, 0, image=ImageTk.PhotoImage(app.background), anchor="nw")
    drawDots(app, canvas)
    # drawPacman
    x, y = app.pacman.center
    canvas.create_image(x, y, image=ImageTk.PhotoImage(
        app.pacmanImg), anchor="c")
    drawGhosts(app, canvas)
    canvas.create_image(
        app.width/2, 757, image=ImageTk.PhotoImage(app.title), anchor="n")
    canvas.create_text(
        app.width/2, 910, text=f"Score: {app.score}", fill="white",
        font="Fixedsys 36 bold")


def drawDots(app, canvas):
    for row in range(len(app.board)):
        for col in range(len(app.board[row])):
            if (app.board[row][col] == " "):
                canvas.create_rectangle(
                    7 + (28 * col), 7 + (28 * row), 15 + (28 * col),
                    15 + (28 * row), fill="white")
            elif (app.board[row][col] == "P"):
                canvas.create_oval(-3 + (28 * col), -3 + (28 * row),
                                   25 + (28 * col), 25 + (28 * row),
                                   fill="white", width=0)
            else:
                canvas.create_rectangle(
                    7 + (28 * col), 7 + (28 * row), 15 + (28 * col),
                    15 + (28 * row), fill="black")


def drawGhosts(app, canvas):
    for i in range(len(app.ghosts)):
        x, y = app.ghosts[i].center
        canvas.create_image(x, y, image=ImageTk.PhotoImage(
            app.ghostImgs[i]), anchor="c")


runApp(width=579, height=940)
