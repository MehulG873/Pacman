from cmu_112_graphics import *
import network
import pickle
import time
from pacman import Pacman
from ghost import *
from datetime import date

# Project: Pacman
# AndrewUserId: mehulg
# Date of Submission: 8/8
# Citations for Image: https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/d9d15482-3751-4b54-b440-93e9202b1c0d/dd7nvab-b2c3ca91-dca6-49e6-b80b-2ce27b20a267.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2Q5ZDE1NDgyLTM3NTEtNGI1NC1iNDQwLTkzZTkyMDJiMWMwZFwvZGQ3bnZhYi1iMmMzY2E5MS1kY2E2LTQ5ZTYtYjgwYi0yY2UyN2IyMGEyNjcucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.1kR9_NEBtyfezx61LNG4PC6SaE3SshPhp_8UmTh49CM 




###############################################################################

def appStarted(app):
    app.mode = 'gameScreen'
    app.powered = False
    app.scores = None
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
    app.ghosts = [dijkstraGhost(app, (10, 10), 0), dijkstraGhost( app, (13, 13), 1), basicGhost(app, (15, 10), 2), playerGhost(app, (13, 7), 3)]
    app.playerGhost = app.ghosts[3]
    app.ghostImgs = []
    for ghost in app.ghosts:
        app.ghostImgs.append(ghost.getImg())
    app.timerDelay = 20
    app.score = 0
    app.paused = True
    app.network = network.network()
    app.playerGhost.dir = app.network.getOtherDir()
    app.send = [str(app.pacman.dir), str(app.pacman.center)]
    
##############################################################################
# Pacman Main Portion of the game
##############################################################################
def gameScreen_keyPressed(app, event):
    if (event.key == "Up"):
        app.pacman.changeDir(2)
    elif (event.key == "Down"):
        app.pacman.changeDir(3)
    elif (event.key == "Left"):
        app.pacman.changeDir(1)
    elif (event.key == "Right"):
        app.pacman.changeDir(0)  
    elif (event.key == "Space"):
        app.network.send("Ready")

def gameScreen_timerFired(app):

    if not app.paused:
        app.send = [str(app.pacman.dir), str(app.pacman.center),
                    str(app.ghosts[0].center),str(app.ghosts[1].center),
                    str(app.ghosts[2].center)]
        data = (app.network.
        send(";".join(app.send)))
        app.playerGhost.dir, center = data.split(";")
        print(app.playerGhost.dir)
        app.playerGhost.dir = eval(app.playerGhost.dir)
        if (center != "0"):
            app.playerGhost.center = eval(center)
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
                    #time.sleep(3)
                    app.mode = "endScreen"
        # app.pacman.nextSprite()
        if (app.board[app.pacman.pos[0]][app.pacman.pos[1]] == " "):
            app.score += 1
            app.board[app.pacman.pos[0]][app.pacman.pos[1]] = "O"
        elif (app.board[app.pacman.pos[0]][app.pacman.pos[1]] == "P"):
            app.score += 10
            app.board[app.pacman.pos[0]][app.pacman.pos[1]] = "O"
            app.powered = True
            app.poweredTime = time.time()
        if time.time() > 7 + app.poweredTime:
            app.powered = False
    else:
        data = app.network.send("Ready?")
        if data == "True":
            app.paused = False
        else:
            print(data)

def getCenter(app, pos):
    cellWidth = app.width/21
    return ((pos[1]-0.5) * cellWidth, (pos[0] - 0.5) * cellWidth)

def gameScreen_redrawAll(app, canvas):
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

##############################################################################
def endScreen_keyPressed(app, event):
    convertScores(app)
    addScore(app)
def endScreen_redrawAll(app, canvas):
    scoresFile = open("scores.txt", "r")
    canvas.create_rectangle(-10, -10, app.width + 10,
                            app.height + 10, fill="black")
    canvas.create_image(
        app.width/2, 0, image=ImageTk.PhotoImage(app.title), anchor="n")
    canvas.create_text(app.width/2, app.height/5, text = "Game Over!",
                    font="Fixedsys 96 bold", fill = "white")
    if (app.scores != None):
        canvas.create_text(app.width/2, app.height/3, text=f"Score: {app.score}",
                       font="Fixedsys 36 bold", fill = "white")
        canvas.create_text(app.width/2, app.height/3 + 50,
                        text = f"Highscores", font="Fixedsys 24",
                        fill = 'white', anchor = "n")
        i = 0
        for line in scoresFile:
            canvas.create_text(app.width/2, app.height/3 + 79 + 29 * i,
                            text = line, font="Fixedsys 24",
                            fill = 'white', anchor = "n")
            i += 1
        if app.score in app.scores and app.scores[app.score] == date.today().strftime("%B %d, %Y"):
            canvas.create_text(app.width/2, 2 * app.height/3,
                            text = "NEW HIGHSCORE", font="Fixedsys 48",
                            fill = 'white', anchor = "n")

    else:
        canvas.create_text(app.width/2, app.height/3, text = "Press Any Key To Continue",
                       font="Fixedsys 24", fill = "white")

def convertScores(app):
    scoresFile = open("scores.txt", "r")
    app.scores = dict()
    for line in scoresFile:
       app.scores[int(line[:line.index(":")])] = line[line.index(" ") + 1:]
def addScore(app):
    #Line 194 date module from https://www.programiz.com/python-programming/datetime/current-datetime 
    app.scores[app.score] = date.today().strftime("%B %d, %Y")
    bestScores = []
    for key in app.scores:
        bestScores.append(key)
        while len(bestScores) > 3:
            bestScores.remove(min(bestScores))
    print(bestScores)
    bestScores.sort(reverse = True)
    scoresFile = open("scores.txt", "w")
    for score in bestScores:
        scoresFile.write(f"{score}: {app.scores[app.score]}\n")

##############################################################################

runApp(width=579, height=940)
