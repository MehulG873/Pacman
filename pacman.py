from cmu_112_graphics import *
from PIL import Image
import time


class Pacman:
    def __init__(self, app, pos):
        self.app = app
        self.pos = pos
        self.dir = 0
        self.spriteCount = 0
        self.spriteImages = [
            self.app.scaleImage(self.app.loadImage(
                'SpriteSheet.png').crop((20, 91, 32, 104)), 2.8),
            self.app.scaleImage(self.app.loadImage(
                'SpriteSheet.png').crop((35, 91, 44, 104)), 2.8),
            self.app.scaleImage(self.app.loadImage(
                'SpriteSheet.png').crop((48, 91, 60, 104)), 2.8),
            self.app.scaleImage(self.app.loadImage(
                'SpriteSheet.png').crop((63, 91, 72, 104)), 2.8),
            self.app.scaleImage(self.app.loadImage(
                'SpriteSheet.png').crop((76, 91, 89, 104)), 2.8),
            self.app.scaleImage(self.app.loadImage(
                'SpriteSheet.png').crop((93, 91, 106, 104)), 2.8),
            self.app.scaleImage(self.app.loadImage(
                'SpriteSheet.png').crop((110, 91, 123, 104)), 2.8),
            self.app.scaleImage(self.app.loadImage(
                'SpriteSheet.png').crop((127, 91, 140, 104)), 2.8)
        ]
        cellWidth = app.width/21
        self.center = (((pos[1]+0.5) * cellWidth, (pos[0] + 0.5) * cellWidth))
        self.speed = 12

    def nextSprite(self):
        self.spriteCount = (self.spriteCount + 1) % 2

    def getImg(self):
        return self.spriteImages[(2 * self.dir) + self.spriteCount]

    def roundPos(self):
        cellWidth = self.app.width/21
        self.center = (((self.pos[1]+0.5) * cellWidth,
                       (self.pos[0] + 0.5) * cellWidth))

    def getPos(self, cord):
        row = round((cord[1]-7)/28)
        col = round((cord[0]-7)/28)
        return row, col

    def changeDir(self, newDir):
        self.dir = newDir
        self.roundPos()

    def move(self):
        dx, dy = 0, 0
        if self.dir == 0:
            dx = self.speed
        elif self.dir == 1:
            dx = -1 * self.speed
        elif self.dir == 2:
            dy = -1 * self.speed
        else:
            dy = self.speed
        newPos = self.getPos((self.center[0] + dx, self.center[1] + dy))
        if newPos[1] < 0 or newPos[1] >= len(self.app.board[0]):
            if self.dir == 0:
                newPos = (newPos[0], 0)
            else:
                newPos = (newPos[0], 20)
            cellWidth = self.app.width/21
            self.center = (((newPos[1]+0.5) * cellWidth,
                           (newPos[0] + 0.5) * cellWidth))
            self.pos = copy.copy(newPos)
            print(self.pos)
            return
        if self.app.board[newPos[0]][newPos[1]] != "X":
            self.center = (self.center[0] + dx, self.center[1] + dy)
            self.pos = self.getPos(self.center)
            self.nextSprite()
