##################
# Cahracters.py Citation Comment
# Structutre of making classes Sprites inspired by Lukas Pereza 112 Blog
# Lines  6 - 69 Original Code
#Lines 69 - 71 Code taken from Lukas Pereza 112 Pygame Blog
# Lines 74 - 80 taken from stack overFlow Link below
# https://stackoverflow.com/questions/50725706/pygame-collision-between-2-objects-in-the-same-group
# Lines 82 - 244 Original Code
##################
import module_manager
module_manager.review()
import pygame
pygame.mixer.init()
import random
import math
width = 500
height = 500
screen = pygame.display.set_mode((width,height))
class Characters(pygame.sprite.Sprite):
    # Every character has a starty point, end point color and image
    def __init__(self, originX, originY, images,color, destinationX, destionationY, direction):
        pygame.sprite.Sprite.__init__(self)
        #super(sprite, self).__init__()
        self.crashSound = pygame.mixer.Sound("car_crash.wav")
        self.direction = direction
        self.timeStopped = 0
        self.cX = originX
        self.cY = originY
        self.imageWidth = 30
        self.imageHeight = 50
        self.images = images
        self.north = pygame.image.load("images/" + self.images[0]).convert_alpha()
        self.north = pygame.transform.scale(self.north, (self.imageWidth,self.imageHeight))
        self.south = pygame.image.load("images/" + self.images[1]).convert_alpha()
        self.south = pygame.transform.scale(self.south, (self.imageWidth,self.imageHeight))
        self.east = pygame.image.load("images/" + self.images[2]).convert_alpha()
        self.east = pygame.transform.scale(self.east, (self.imageHeight,self.imageWidth))
        self.west = pygame.image.load("images/" + self.images[3]).convert_alpha()
        self.west = pygame.transform.scale(self.west, (self.imageHeight,self.imageWidth))
        self.color = color
        self.destinationX = destinationX
        self.destinationY = destionationY
        self.rect = pygame.Rect(self.cX - self.imageWidth/ 2, self.cY - self.imageHeight / 2, self.imageWidth, self.imageHeight)
        #self.rect = pygame.Rect(self.cX,self.cY,self.imageWidth,self.imageHeight)
    def __repr__(self):
        return "Image at " + str(self.cX) + " " + str(self.cY) + " " + self.direction
    # def __hash__(self,other):
    #     return isinstance(other,self)
    def getCordinates(self):
        return (self.cX, self.cY)
    def getDimensions(self):
        return (self.imageWidth,self.imageHeight)
    def drawMe(self,screen , orientation):
        screen.blit(self.image, (self.cX, self.cY))
    def idle(self):
        return self.timeStopped
    def addTime(self):
        self.timeStopped += 1
    def updateRect(self):
        self.rect = pygame.Rect(self.cX - self.imageWidth/ 2, \
         self.cY - self.imageHeight / 2, self.imageWidth, self.imageHeight)
    def checkCollisions(self, others):
        for sprite in others:
            if sprite is self:
                continue
            elif self.rect.colliderect(sprite.rect):
                pygame.mixer.Sound.play(self.crashSound)
                return True
        return False
class Car(Characters):
    def __init__(self, startX, startY, images, finishX, finishY, color, direction):
        super(Car, self).__init__(startX, startY, images,color,finishX, finishY,direction)
        self.speed = 6
        self.direction = str(direction)
    def getSpeed(self):
        return self.speed
    def stop(self):
        self.cY += 0
        self.cX += 0
    def getDirection(self):
        return "Direction " + str(self.direction)
    def moveUp(self):
        self.cY -= self.speed
    def moveDown(self):
        self.cY += self.speed
    def moveRight(self):
        self.cX += self.speed
    def moveLeft(self):
        self.cX -= self.speed
    def __repr__(self):
        return "Image at " + str(self.cX) + " " + str(self.cY) + " " + self.getDirection()
    def drawMe(self,screen , orientation):
        if self.getDirection() == "Direction NORTH":
            screen.blit(self.north, (self.cX, self.cY))
        if self.getDirection() == 'Direction SOUTH':
            screen.blit(self.south, (self.cX,self.cY))
        if self.getDirection() == "Direction EAST":
            screen.blit(self.east, (self.cX,self.cY))
        if self.getDirection() == "Direction WEST":
            screen.blit(self.west, (self.cX, self.cY))
class TrafficLights(Characters):
    def __init__(self,x,y,width,height, orientation, status, cardinal):
        self.x = x
        self.y = y
        self.status = status
        self.orientation = orientation
        self.width = width
        self.height = height
        self.greenOn = 50,255,50
        self.greenOff = 0,120,50
        self.redOn = 255,0,0
        self.redOff = 140,0,0
        self.cardinal = cardinal
        if self.status:
            self.green = True
            self.red = False
        else:
            self.green = False
            self.red = True
    def __repr__(self):
        return "Facing " + str(self.cardinal) + " " + str(self.status)
    def whatCardinal(self):
        return self.cardinal
    def changeLight(self):
        self.green = not self.green
        self.red = not self.red
        self.status = not self.status
    def currentStatus(self):
        if self.green:
            return True
        if self.red:
            return False
    def drawLight(self, screen):
        if self.orientation == "Horizontal":
            #pygame.draw.rect(screen, (139,137,137), (self.x, self.y, self.width,self.height))
            if self.green:
                pygame.draw.rect(screen, (self.greenOn), (self.x, self.y, self.width,self.height))
            if self.red:
                pygame.draw.rect(screen, (self.redOn), (self.x, self.y, self.width,self.height))
                # pygame.draw.circle(screen, (self.greenOff), (self.x + 20, self.y + self.height//2), 15)
                # pygame.draw.circle(screen, (self.redOn),(self.x + 80, self.y + self.height//2), 15)
        if self.orientation == "Vertical":
            pygame.draw.rect(screen, (139,137,137), (self.x,self.y,self.height,self.width))
            if self.green:
                pygame.draw.rect(screen, (self.greenOn), (self.x,self.y,self.height,self.width))
                # pygame.draw.circle(screen, (self.greenOn), (self.x + 20, self.y + 20), 15)
                # pygame.draw.circle(screen, (self.redOff), (self.x + 20, self.y + 80), 15)
            if self.red:
                pygame.draw.rect(screen, (self.redOn), (self.x,self.y,self.height,self.width))
                # pygame.draw.circle(screen, (self.greenOff), (self.x + 20, self.y + 20), 15)
                # pygame.draw.circle(screen, (self.redOn), (self.x + 20, self.y + 80), 15)
    def getPosition(self):
        return (self.x,self.y,self.width,self.height)
