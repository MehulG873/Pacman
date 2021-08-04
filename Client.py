from cmu_112_graphics import *


def appStarted(app):
    app.image1 = app.loadImage('SpriteSheet.png')
    app.image2 = 


def redrawAll(app, canvas):
    canvas.create_image(
        200, 300, image=ImageTk.PhotoImage(app.image1), anchor="nw")


runApp(width=700, height=600)
