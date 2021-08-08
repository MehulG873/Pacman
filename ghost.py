from cmu_112_graphics import *
from PIL import Image
import random

class Ghost:
    def __init__(self, app, pos, color):
        self.app = app
        self.pos = pos
        self.dir = 0
        self.color = color
        self.spriteCount = 0
        self.spriteImages = [
                             self.app.scaleImage(self.app.loadImage('SpriteSheet.png').crop((3 + 17 *i, 125 + 18 * color, 17 + 17*i, 138 + 18 * color)), 2.8) for i in range(8)
                            ]
        cellWidth = app.width/21
        self.center = (((pos[1]+0.5) * cellWidth, (pos[0] + 0.5) * cellWidth))
        self.speed = 7 + color
        self.previousMoves = []
        self.app.scared = self.app.scaleImage(self.app.loadImage('SpriteSheet.png').crop((3, 125 + 18 * 4, 17, 138 + 18 * 4)), 2.8)
    def nextSprite(self):
        self.spriteCount = (self.spriteCount + 1)%2

    def getImg(self):
        if self.app.powered:
            return self.app.scared
        else:
            return self.spriteImages[(2 * self.dir) + self.spriteCount]

    def getPos(self, cord):
        row = round((cord[1]-7)/28) 
        col = round((cord[0]-7)/28)
        return row, col
    def changeDir(self, newDir):
        self.dir = newDir

    def move(self):
        self.evaluateDirection()
        dx, dy = 0,0
        if self.dir == 0:
            dx = self.speed
        elif self.dir == 1:
            dx = -1 * self.speed
        elif self.dir == 2:
            dy = -1 * self.speed
        else:
            dy = self.speed
        newPos = self.getPos((self.center[0] + dx, self.center[1] + dy))
        if self.app.board[newPos[0]][newPos[1]] != "X":
            self.center = (self.center[0] + dx, self.center[1] + dy)
            if self.getPos(self.center) != self  .pos:
                self.previousMoves.append(self.getPos(self.center))
                if (len(self.previousMoves) > 5):
                    self.previousMoves.pop(0)
            self.pos = self.getPos(self.center)
            self.nextSprite()
    def evaluateDirection(self):
        self.changeDir(random.randint(0, 3))
    @staticmethod
    def getDistance(p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
class randomGhost(Ghost):
    def evaluateDirection(self):
        self.changeDir(random.randint(0, 3))

class basicGhost(Ghost):
    def evaluateDirection(self):
        if not self.app.powered:
            self.speed = 7 + self.color
            possibleDirections = []
            for x in range(-1, 2, 2):
                if (self.pos[1] + x >= 0 and self.pos[1] + x <= 21 and 
                    self.app.board[self.pos[0]][self.pos[1] + x] != "X"):
                    if x < 0:
                        possibleDirections.append(1)
                    else:
                        possibleDirections.append(0)
            for y in range(-1, 2, 2):
                if (self.pos[0] + y >= 0 and self.pos[0] + y <= 25 and 
                    self.app.board[self.pos[0] + y][self.pos[1]] != "X"):
                    if y < 0:
                        possibleDirections.append(2)
                    else:
                        possibleDirections.append(3)
            possibleMoves = dict()
            for direction in possibleDirections:
                distanceToPacman = 0
                if direction < 2:
                    newPos = (self.pos[0], self.pos[1] + ((1 - direction) * 2 -1))
                else:
                    newPos = (self.pos[0] + (direction%2 * 2) -1, self.pos[1])
                distanceToPacman = Ghost.getDistance(self.app.pacman.pos, newPos)
                if newPos in self.previousMoves:
                    continue
                possibleMoves[direction] = distanceToPacman  
                print(f"For Dir: {direction} New Pos: {newPos} Pacman Pos: {self.app.pacman.pos}")
            minDistance = 1000000
            minDir = 0
            for key in possibleMoves:
                if (possibleMoves[key] < minDistance):
                    minDistance = possibleMoves[key]
                    minDir = key
                    print(f"Key: {key} MinDir: {minDir} minDistance: {minDistance}")
                elif possibleMoves[key] == minDistance:
                    minDir = key
                else:
                    print(f"Key: {key} MinDir: {minDir} Distance: {possibleMoves[key]}")
            print(minDir)
            self.changeDir(minDir)
        else:
            self.speed = 9 + self.color
            possibleDirections = []
            for x in range(-1, 2, 2):
                if (self.pos[1] + x >= 0 and self.pos[1] + x <= 21 and 
                    self.app.board[self.pos[0]][self.pos[1] + x] != "X"):
                    if x < 0:
                        possibleDirections.append(1)
                    else:
                        possibleDirections.append(0)
            for y in range(-1, 2, 2):
                if (self.pos[0] + y >= 0 and self.pos[0] + y <= 25 and 
                    self.app.board[self.pos[0] + y][self.pos[1]] != "X"):
                    if y < 0:
                        possibleDirections.append(2)
                    else:
                        possibleDirections.append(3)
            possibleMoves = dict()
            for direction in possibleDirections:
                distanceToPacman = 0
                if direction < 2:
                    newPos = (self.pos[0], self.pos[1] + ((1 - direction) * 2 -1))
                else:
                    newPos = (self.pos[0] + (direction%2 * 2) -1, self.pos[1])
                distanceToPacman = Ghost.getDistance(self.app.pacman.pos, newPos)
                if newPos in self.previousMoves:
                    continue
                possibleMoves[direction] = distanceToPacman  
                print(f"For Dir: {direction} New Pos: {newPos} Pacman Pos: {self.app.pacman.pos}")
            maxDistance = 0
            maxDir = 0
            for key in possibleMoves:
                if (possibleMoves[key] > maxDistance):
                    maxDistance = possibleMoves[key]
                    maxDir = key
                    print(f"Key: {key} MaxDir: {maxDir} maxDistance: {maxDistance}")
                elif possibleMoves[key] == maxDistance:
                    maxDir = key
                else:
                    print(f"Key: {key} MaxDir: {maxDir} Distance: {possibleMoves[key]}")
            print(maxDir)
            self.changeDir(maxDir)