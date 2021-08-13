# Project: Pacman
# AndrewUserId: mehulg
# Date of Submission: 8/8
# Citations for Image: https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/d9d15482-3751-4b54-b440-93e9202b1c0d/dd7nvab-b2c3ca91-dca6-49e6-b80b-2ce27b20a267.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2Q5ZDE1NDgyLTM3NTEtNGI1NC1iNDQwLTkzZTkyMDJiMWMwZFwvZGQ3bnZhYi1iMmMzY2E5MS1kY2E2LTQ5ZTYtYjgwYi0yY2UyN2IyMGEyNjcucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.1kR9_NEBtyfezx61LNG4PC6SaE3SshPhp_8UmTh49CM
# Citations for plyaing music. Music Library: https://www.sounds-resource.com/arcade/pacman/sound/10603/
# Playing Music Tutorial: https://pythonprogramming.net/adding-sounds-music-pygame/


###############################################################################
from cmu_112_graphics import *
from pacman import Pacman
from ghost import *
import time
from datetime import date
import network
import pygame


def appStarted(app):
    pygame.mixer.init()
    app.mode = 'homeScreen'
    app.powered = False
    app.scores = None
    app.board = [["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                 ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X",
                     " ", " ", " ", " ", " ", " ", " ", " ", " ", "X"],
                 ["X", " ", "X", "X", "X", " ", "X", "X", "X", " ", "X",
                     " ", "X", "X", "X", " ", "X", "X", "X", " ", "X"],
                 ["X", "P", "X", "X", "X", " ", "X", "X", "X", " ", "X",
                     " ", "X", "X", "X", " ", "X", "X", "X", "P", "X"],
                 ["X", " ", "X", "X", "X", " ", "X", "X", "X", " ", "X",
                     " ", "X", "X", "X", " ", "X", "X", "X", " ", "X"],
                 ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                     " ", " ", " ", " ", " ", " ", " ", " ", " ", "X"],
                 ["X", " ", "X", "X", "X", " ", "X", " ", "X", "X", "X",
                     "X", "X", " ", "X", " ", "X", "X", "X", " ", "X"],
                 ["X", " ", "X", "X", "X", " ", "X", " ", "X", "X", "X",
                     "X", "X", " ", "X", " ", "X", "X", "X", " ", "X"],
                 ["X", " ", " ", " ", " ", " ", "X", " ", " ", " ", "X",
                     " ", " ", " ", "X", " ", " ", " ", " ", " ", "X"],
                 ["X", "X", "X", "X", "X", " ", "X", "X", "X", "O", "X",
                     "O", "X", "X", "X", " ", "X", "X", "X", "X", "X"],
                 ["X", "X", "X", "X", "X", " ", "X", "O", "O", "O", "O",
                     "O", "O", "O", "X", " ", "X", "X", "X", "X", "X"],
                 ["X", "X", "X", "X", "X", " ", "X", "O", "X", "X", "X",
                     "X", "X", "O", "X", " ", "X", "X", "X", "X", "X"],
                 ["X", "X", "X", "X", "X", " ", "X", "O", "X", "X", "X",
                     "X", "X", "O", "X", " ", "X", "X", "X", "X", "X"],
                 ["O", "O", "O", "O", "O", " ", "O", "O", "X", "X", "X",
                     "X", "X", "O", "O", " ", "O", "O", "O", "O", "O"],
                 ["X", "X", "X", "X", "X", " ", "X", "O", "X", "X", "X",
                     "X", "X", "O", "X", " ", "X", "X", "X", "X", "X"],
                 ["X", "X", "X", "X", "X", " ", "X", "O", "O", "O", "O",
                     "O", "O", "O", "X", " ", "X", "X", "X", "X", "X"],
                 ["X", "X", "X", "X", "X", " ", "X", "O", "X", "X", "X",
                     "X", "X", "O", "X", " ", "X", "X", "X", "X", "X"],
                 ["X", "X", "X", "X", "X", " ", "X", " ", "X", "X", "X",
                     "X", "X", " ", "X", " ", "X", "X", "X", "X", "X"],
                 ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X",
                     " ", " ", " ", " ", " ", " ", " ", " ", " ", "X"],
                 ["X", " ", "X", "X", "X", " ", "X", "X", "X", " ", "X",
                     " ", "X", "X", "X", " ", "X", "X", "X", " ", "X"],
                 ["X", "P", " ", " ", "X", " ", " ", " ", " ", " ", "O",
                     " ", " ", " ", " ", " ", "X", " ", " ", "P", "X"],
                 ["X", "X", "X", " ", "X", " ", "X", " ", "X", "X", "X",
                     "X", "X", " ", "X", " ", "X", " ", "X", "X", "X"],
                 ["X", "X", "X", " ", "X", " ", "X", " ", "X", "X", "X",
                     "X", "X", " ", "X", " ", "X", " ", "X", "X", "X"],
                 ["X", " ", " ", " ", " ", " ", "X", " ", " ", " ", "X",
                     " ", " ", " ", "X", " ", " ", " ", " ", " ", "X"],
                 ["X", " ", "X", "X", "X", "X", "X", "X", "X", " ", "X",
                     " ", "X", "X", "X", "X", "X", "X", "X", " ", "X"],
                 ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                     " ", " ", " ", " ", " ", " ", " ", " ", " ", "X"],
                 ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X",
                     "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                 ]
    app.poweredTime = time.time()
    app.background = app.  scaleImage(app.loadImage(
        'SpriteSheet.png').crop((370, 3, 530, 216)), 3)
    app.dot = app.scaleImage(app.loadImage(
        'SpriteSheet.png').crop((3, 81, 5, 83)), 3)
    app.blank = app.scaleImage(app.loadImage(
        'SpriteSheet.png').crop((5, 81, 7, 83)), 3)
    app.pacman = Pacman(app, (20, 10))
    app.pacmanImg = app.pacman.getImg()
    app.title = app.scaleImage(app.loadImage(
        'SpriteSheet.png').crop((2, 4, 184, 50)), 2.6)
    app.ghosts = [randomGhost(app, (10, 10), 0), basicGhost(
        app, (13, 13), 1), dijkstraGhost(app, (15, 10), 2), dijkstraGhost(app, (13, 7), 3)]
    app.playerGhost = app.ghosts[3]
    app.ghostImgs = []
    for ghost in app.ghosts:
        app.ghostImgs.append(ghost.getImg())
    app.startSound = pygame.mixer.Sound("Sounds/game_start.wav")
    app.death = pygame.mixer.Sound("Sounds/death_1.wav")
    app.eatGhost = pygame.mixer.Sound("Sounds/eat_ghost.wav")
    app.munch1 = pygame.mixer.Sound("Sounds/munch_1.wav")
    app.munch2 = pygame.mixer.Sound("Sounds/munch_2.wav")
    app.powerPellet = pygame.mixer.Sound("Sounds/power_pellet.wav")
    app.intermission = pygame.mixer.Sound("Sounds/intermission.wav")
    app.timerDelay = 20
    app.score = 0
    app.paused = True
##############################################################################
# Home Screen Main Portion of the game
##############################################################################


def homeScreen_redrawAll(app, canvas):
    if not pygame.mixer.get_busy():
        pygame.mixer.Sound.play(app.startSound)
    canvas.create_rectangle(-10, -10, app.width + 10,
                            app.height + 10, fill="black")
    canvas.create_image(
        app.width/2, 10, image=ImageTk.PhotoImage(app.title), anchor="n")
    canvas.create_text(app.width/2, 140, text="-MEHUL GOEL",
                       anchor="n", fill="white", font="Fixedsys 30 bold")

    # Draw SinglePlayer
    canvas.create_rectangle(50, 250, app.width - 50, 350, fill="gold")
    canvas.create_text(app.width/2, 300, text="SINGLE PLAYER",
                       anchor="c", fill="white", font="Fixedsys 30 bold")

    # Draw PacmanMultiplayer
    canvas.create_rectangle(50, 425, app.width - 50, 525, fill="orange")
    canvas.create_text(app.width/2, 475, text="PACMAN MULTI",
                       anchor="c", fill="white", font="Fixedsys 30 bold")

    # Draw SinglePlayer
    canvas.create_rectangle(50, 600, app.width - 50, 700, fill="OrangeRed")
    canvas.create_text(app.width/2, 650, text="GHOST MULTI",
                       anchor="c", fill="white", font="Fixedsys 30 bold")


def homeScreen_mousePressed(app, event):
    if (50 < event.x < app.width - 50):
        if (250 < event.y < 350):
            app.mode = 'singlePlayer'
        elif (425 < event.y < 525):
            app.playerGhost = playerGhost(app, (13, 7), 3)
            app.ghosts[3] = app.playerGhost
            for ghost in app.ghosts:
                app.ghostImgs.append(ghost.getImg())
            app.network = network.network()
            app.playerGhost.dir = app.network.getOtherDir()
            app.send = [app.pacman.dir, app.pacman.center]
            app.mode = 'pacmanMulti'
        elif (600 < event.y < 700):
            app.playerGhost = playerGhost(app, (13, 7), 3)
            app.ghosts[3] = app.playerGhost
            for ghost in app.ghosts:
                app.ghostImgs.append(ghost.getImg())
            app.network = network.network()
            app.pacman.dir = int(app.network.getOtherDir())
            app.send = [str(app.playerGhost.dir), str(app.playerGhost.center)]
            app.mode = 'ghostMulti'


##############################################################################
# Pacman Main Portion of the game
##############################################################################
def singlePlayer_keyPressed(app, event):
    if (event.key == "Up"):
        app.paused = False
        app.pacman.changeDir(2)
    elif (event.key == "Down"):
        app.paused = False
        app.pacman.changeDir(3)
    elif (event.key == "Left"):
        app.paused = False
        app.pacman.changeDir(1)
    elif (event.key == "Right"):
        app.paused = False
        app.pacman.changeDir(0)


def singlePlayer_timerFired(app):
    if not app.paused:
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
                    pygame.mixer.Sound.play(app.eatGhost)
                else:
                    # time.sleep(3)
                    pygame.mixer.Sound.play(app.death)
                    app.mode = "endScreen"
        # app.pacman.nextSprite()
        if (app.board[app.pacman.pos[0]][app.pacman.pos[1]] == " "):
            if not pygame.mixer.get_busy():
                pygame.mixer.Sound.play(app.munch1)
            app.score += 1
            app.board[app.pacman.pos[0]][app.pacman.pos[1]] = "O"
        elif (app.board[app.pacman.pos[0]][app.pacman.pos[1]] == "P"):
            app.score += 10
            app.board[app.pacman.pos[0]][app.pacman.pos[1]] = "O"
            app.powered = True
            app.poweredTime = time.time()
            pygame.mixer.Sound.play(app.powerPellet)
        if time.time() > 7 + app.poweredTime:
            app.powered = False


def singlePlayer_getCenter(app, pos):
    cellWidth = app.width/21
    return ((pos[1]-0.5) * cellWidth, (pos[0] - 0.5) * cellWidth)


def singlePlayer_redrawAll(app, canvas):
    canvas.create_rectangle(-10, -10, app.width + 10,
                            app.height + 10, fill="black")
    canvas.create_image(
        0, 0, image=ImageTk.PhotoImage(app.background), anchor="nw")
    singlePlayer_drawDots(app, canvas)
    # drawPacman
    x, y = app.pacman.center
    canvas.create_image(x, y, image=ImageTk.PhotoImage(
        app.pacmanImg), anchor="c")
    singlePlayer_drawGhosts(app, canvas)
    canvas.create_image(
        app.width/2, 650, image=ImageTk.PhotoImage(app.title), anchor="n")
    canvas.create_text(
        app.width/2, 800, text=f"Score: {app.score}", fill="white",
        font="Fixedsys 30 bold")


def singlePlayer_drawDots(app, canvas):
    for row in range(len(app.board)):
        for col in range(len(app.board[row])):
            if (app.board[row][col] == " "):
                canvas.create_rectangle(
                    5 + (24 * col), 5 + (24 * row), 13 + (24 * col),
                    13 + (24 * row), fill="white")
            elif (app.board[row][col] == "P"):
                canvas.create_oval(-1 + (24 * col), -1 + (24 * row),
                                   23 + (24 * col), 23 + (24 * row),
                                   fill="white", width=0)
            else:
                canvas.create_rectangle(
                    5 + (24 * col), 5 + (24 * row), 13 + (24 * col),
                    13 + (24 * row), fill="black")


def singlePlayer_drawGhosts(app, canvas):
    for i in range(len(app.ghosts)):
        x, y = app.ghosts[i].center
        canvas.create_image(x, y, image=ImageTk.PhotoImage(
            app.ghostImgs[i]), anchor="c")

##############################################################################
# Pacman Multiplayer
##############################################################################


def pacmanMulti_keyPressed(app, event):
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


def pacmanMulti_timerFired(app):
    if not app.paused:
        app.send = [str(app.pacman.dir), str(app.pacman.center),
                    str(app.ghosts[0].center), str(app.ghosts[1].center),
                    str(app.ghosts[2].center), str(app.score)]
        data = (app.network.
                send(";".join(app.send)))
        print(f"Data = {data}")
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
                    pygame.mixer.Sound.play(app.eatGhost)
                else:
                    # time.sleep(3)
                    pygame.mixer.Sound.play(app.death)
                    app.mode = "endScreen"
        # app.pacman.nextSprite()
        if (app.board[app.pacman.pos[0]][app.pacman.pos[1]] == " "):
            app.score += 1
            app.board[app.pacman.pos[0]][app.pacman.pos[1]] = "O"
            if not pygame.mixer.get_busy():
                pygame.mixer.Sound.play(app.munch1)
        elif (app.board[app.pacman.pos[0]][app.pacman.pos[1]] == "P"):
            app.score += 10
            app.board[app.pacman.pos[0]][app.pacman.pos[1]] = "O"
            app.powered = True
            app.poweredTime = time.time()
            pygame.mixer.Sound.play(app.powerPellet)
        if time.time() > 7 + app.poweredTime:
            app.powered = False
    else:
        data = app.network.send("Ready?")
        if data == "True":
            app.paused = False
        else:
            print(data)


def pacmanMulti_getCenter(app, pos):
    cellWidth = app.width/21
    return ((pos[1]-0.5) * cellWidth, (pos[0] - 0.5) * cellWidth)


def pacmanMulti_redrawAll(app, canvas):
    canvas.create_rectangle(-10, -10, app.width + 10,
                            app.height + 10, fill="black")
    canvas.create_image(
        0, 0, image=ImageTk.PhotoImage(app.background), anchor="nw")
    pacmanMulti_drawDots(app, canvas)
    # drawPacman
    x, y = app.pacman.center
    canvas.create_image(x, y, image=ImageTk.PhotoImage(
        app.pacmanImg), anchor="c")
    pacmanMulti_drawGhosts(app, canvas)
    canvas.create_image(
        app.width/2, 650, image=ImageTk.PhotoImage(app.title), anchor="n")
    canvas.create_text(
        app.width/2, 800, text=f"Score: {app.score}", fill="white",
        font="Fixedsys 30 bold")


def pacmanMulti_drawDots(app, canvas):
    for row in range(len(app.board)):
        for col in range(len(app.board[row])):
            if (app.board[row][col] == " "):
                canvas.create_rectangle(
                    5 + (24 * col), 5 + (24 * row), 13 + (24 * col),
                    13 + (24 * row), fill="white")
            elif (app.board[row][col] == "P"):
                canvas.create_oval(-1 + (24 * col), -1 + (24 * row),
                                   23 + (24 * col), 23 + (24 * row),
                                   fill="white", width=0)
            else:
                canvas.create_rectangle(
                    5 + (24 * col), 5 + (24 * row), 13 + (24 * col),
                    13 + (24 * row), fill="black")


def pacmanMulti_drawGhosts(app, canvas):
    for i in range(len(app.ghosts)):
        x, y = app.ghosts[i].center
        canvas.create_image(x, y, image=ImageTk.PhotoImage(
            app.ghostImgs[i]), anchor="c")
##############################################################################
# Ghost Multiplayer
##############################################################################


def ghostMulti_keyPressed(app, event):
    if (event.key == "Up"):
        app.playerGhost.changeDir(2)
    elif (event.key == "Down"):
        app.playerGhost.changeDir(3)
    elif (event.key == "Left"):
        app.playerGhost.changeDir(1)
    elif (event.key == "Right"):
        app.playerGhost.changeDir(0)
    elif (event.key == "Space"):
        app.network.send("Ready")


def ghostMulti_timerFired(app):
    if not app.paused:
        app.send = [str(app.playerGhost.dir),
                    str(app.playerGhost.center)]
        app.received = (app.network.
                        send(";".join(app.send)).split(";"))
        if app.received != ['0']:
            print(repr(app.received))
            ghostMulti_unpackReceived(app, app.received)
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
                    pygame.mixer.Sound.play(app.eatGhost)
                else:
                    # time.sleep(3)
                    pygame.mixer.Sound.play(app.death)
                    app.mode = "endScreen"
        # app.pacman.nextSprite()
        if (app.board[app.pacman.pos[0]][app.pacman.pos[1]] == " "):
            app.score += 1
            app.board[app.pacman.pos[0]][app.pacman.pos[1]] = "O"
            if not pygame.mixer.get_busy():
                pygame.mixer.Sound.play(app.munch1)
        elif (app.board[app.pacman.pos[0]][app.pacman.pos[1]] == "P"):
            app.score += 10
            app.board[app.pacman.pos[0]][app.pacman.pos[1]] = "O"
            app.powered = True
            app.poweredTime = time.time()
            pygame.mixer.Sound.play(app.powerPellet)
        if time.time() > 7 + app.poweredTime:
            app.powered = False
    else:
        data = app.network.send("Ready?")
        if data == "True":
            app.paused = False
        else:
            print(data)


def ghostMulti_unpackReceived(app, received):
    print("UNPACKING\n")
    print(repr(received))
    app.pacman.dir = eval(received[0])
    print(repr(received[0]))
    app.pacman.center = eval(received[1])
    app.ghosts[0].center = eval(received[2])
    app.ghosts[1].center = eval(received[3])
    app.ghosts[2].center = eval(received[4])
    app.score = eval(received[5])


def ghostMulti_getCenter(app, pos):
    cellWidth = app.width/21
    return ((pos[1]-0.5) * cellWidth, (pos[0] - 0.5) * cellWidth)


def ghostMulti_redrawAll(app, canvas):
    canvas.create_rectangle(-10, -10, app.width + 10,
                            app.height + 10, fill="black")
    canvas.create_image(
        0, 0, image=ImageTk.PhotoImage(app.background), anchor="nw")
    ghostMulti_drawDots(app, canvas)
    # drawPacman
    x, y = app.pacman.center
    canvas.create_image(x, y, image=ImageTk.PhotoImage(
        app.pacmanImg), anchor="c")
    ghostMulti_drawGhosts(app, canvas)
    canvas.create_image(
        app.width/2, 650, image=ImageTk.PhotoImage(app.title), anchor="n")
    canvas.create_text(
        app.width/2, 800, text=f"Score: {app.score}", fill="white",
        font="Fixedsys 30 bold")


def ghostMulti_drawDots(app, canvas):
    for row in range(len(app.board)):
        for col in range(len(app.board[row])):
            if (app.board[row][col] == " "):
                canvas.create_rectangle(
                    5 + (24 * col), 5 + (24 * row), 13 + (24 * col),
                    13 + (24 * row), fill="white")
            elif (app.board[row][col] == "P"):
                canvas.create_oval(-1 + (24 * col), -1 + (24 * row),
                                   23 + (24 * col), 23 + (24 * row),
                                   fill="white", width=0)
            else:
                canvas.create_rectangle(
                    5 + (24 * col), 5 + (24 * row), 13 + (24 * col),
                    13 + (24 * row), fill="black")


def ghostMulti_drawGhosts(app, canvas):
    for i in range(len(app.ghosts)):
        x, y = app.ghosts[i].center
        canvas.create_image(x, y, image=ImageTk.PhotoImage(
            app.ghostImgs[i]), anchor="c")

##############################################################################


def endScreen_keyPressed(app, event):
    app.scores = None
    convertScores(app)
    addScore(app)


def endScreen_redrawAll(app, canvas):
    if not pygame.mixer.get_busy():
        pygame.mixer.Sound.play(app.intermission)
    scoresFile = open("scores.txt", "r")
    canvas.create_rectangle(-10, -10, app.width + 10,
                            app.height + 10, fill="black")
    canvas.create_image(
        app.width/2, 0, image=ImageTk.PhotoImage(app.title), anchor="n")
    canvas.create_text(app.width/2, app.height/5, text="Game Over!",
                       font="Fixedsys 96 bold", fill="white")
    if (app.scores != None):
        canvas.create_text(app.width/2, app.height/3, text=f"Score: {app.score}",
                           font="Fixedsys 30 bold", fill="white")
        canvas.create_text(app.width/2, app.height/3 + 50,
                           text=f"Highscores", font="Fixedsys 24",
                           fill='white', anchor="n")
        i = 0
        for line in scoresFile:
            canvas.create_text(app.width/2, app.height/3 + 79 + 29 * i,
                               text=line, font="Fixedsys 24",
                               fill='white', anchor="n")
            i += 1
        if app.isHighScore:
            canvas.create_text(app.width/2, 2 * app.height/3,
                               text="NEW HIGHSCORE", font="Fixedsys 30",
                               fill='white', anchor="n")

    else:
        canvas.create_text(app.width/2, app.height/3, text="Press Any Key To Continue",
                           font="Fixedsys 24", fill="white")


def convertScores(app):
    scoresFile = open("scores.txt", "r")
    app.scores = dict()
    for line in scoresFile:
        app.scores[int(line[:line.index(":")])] = line[line.index(" ") + 1:]


def addScore(app):
    # Line 194 date module from https://www.programiz.com/python-programming/datetime/current-datetime
    app.scores[app.score] = date.today().strftime("%B %d, %Y") + "\n"
    print(app.scores)
    bestScores = []
    app.isHighScore = True
    print(app.scores)
    for key in app.scores:
        bestScores.append(key)
    print(app.scores)
    while len(bestScores) > 3:
        if (min(bestScores) == app.score):
            app.isHighScore = False
        else:
            app.isHighScore = True
        bestScores.remove(min(bestScores))
    # print(bestScores)
    print(app.scores)
    bestScores.sort(reverse=True)
    scoresFile = open("scores.txt", "w")
    for score in bestScores:
        scoresFile.write(f"{score}: {app.scores[score]}")

##############################################################################


runApp(width=500, height=850)
