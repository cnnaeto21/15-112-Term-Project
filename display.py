#########################################
#Display.py Citation Comment:
#Lines 7-188: Original code
#Lines 213-285: Event Handler stucture taken from https://github.com/OrionDark7/pyweek26/blob/master/main.py
# Lines 287 - 291 Calling run function taken from 112 homeworks
#########################################
import module_manager
module_manager.ignore_module('level1')
module_manager.ignore_module('level2')
module_manager.ignore_module('level3')
module_manager.ignore_module('survival')
module_manager.ignore_module('starterScreen')
module_manager.ignore_module('characters.py')
module_manager.review()
import pygame
#pygame.font.get_fonts()
import random
import math
from characters import TrafficLights, Car
from starterScreen import *
from level1 import *
from level2 import *
from level3 import *
from survival import *
#from levels import level1Board
import images
########### Game Initializer ########
pygame.init()
pygame.font.init()
pygame.font.get_fonts()
pygame.mixer.init()
pygame.mixer.music.load("Traffic-7.wav")
####################################
fps = 100
width = 1280
height = 700
green = (0,100,0)
red = (255,0,0)
black = (0,0,0)
beige = (250,250,210)
ScoreFont = pygame.font.SysFont("Verdana", 25)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
starterScreen = StarterScreen(width, height)
gameOptionsScreen = GameOptions(width, height)
instructionsScreen = Instructions(width, height)
def init(data):
    data.stop = False
    data.score = 0
    data.gameOver = False
    data.gameMode = "starter"
    data.margin = 40
    data.imageWidth = 30
    data.imageHeight = 50
    data.width = width
    data.height = height
    data.trafficLights = [ TrafficLights(data.width//2 - 85, data.height - data.height//2 + 85, 170,20, \
    "Horizontal", True, "north"),
    TrafficLights(data.width//2 - 120, data.height//2 - 85, 170,20, "Vertical", False, "east"),
    TrafficLights(data.width//2 + 110, data.height//2 - 85, 170, 20, "Vertical", False, "west"),
    TrafficLights(data.width//2 - 85, data.height - data.height//2 - 105, 170,20, "Horizontal", True, "south")
    ]
    data.objects = []
    data.spriteObjects = pygame.sprite.Group()
    data.vehicleOptions = [ "Car" ]
    data.spawnPoint1 = ((data.width//2 + 25),(data.height - data.imageHeight//2),"NORTH")
    data.spawnPoint2 = (data.width//2 - 50 ,data.imageHeight - 25 , "SOUTH")
    data.spawnPoint3 = (data.imageWidth//2, data.height//2 + 35, "EAST")
    data.spawnPoint4 = ((data.width - data.imageHeight//2),data.height//2 - 45, "WEST")
    data.spawnPoints = [data.spawnPoint1, data.spawnPoint2, data.spawnPoint3, data.spawnPoint4]
    data.blue = 25,25,112
    data.yellow = 255,255,0
    data.red = 255,0,0
    data.black = 255,255,255
    data.current = None
    data.colors = ["blue", "red", "pink", "green"]
    #Make a dictionary of colors with their images already in it
    data.images = { "blue":['blueCar.png', 'blueCarSouth.png','blueCarWest.png', 'blueCarEast.png'],
    "red": ['redCarNorth.png', 'redCarSouth.png', 'redCarWest.png', 'redCarEast.png'],
    "green": ['greenCarNorth.png', 'greenCarSouth.png', 'greenCarWest.png', 'greenCarEast.png'],
    'pink': ['pinkCarNorth.png', 'pinkCarSouth.png', 'pinkCarWest.png', 'pinkCarEast.png']
     }
def lightFacing(data, direction):
    for light in data.trafficLights:
        if light.whatCardinal() == direction:
            return light
def timerFiredNewCharacter(data):
    takenSpots = [False,False,False,False]
    for object in data.objects:
        if object.getDirection() == "Direction NORTH":
            if (data.height - data.imageHeight//2) - object.getCordinates()[1] < 45:
                takenSpots[0] = True #not takenSpots[0]
            else:
                takenSpots[0] = False # not takenSpots[0]
        if object.getDirection() == "Direction SOUTH":
            if object.getCordinates()[1] - (data.imageHeight - 25) < 45:
                takenSpots[1] = True # not takenSpots[1]
            else:
                takenSpots[1] = False #not takenSpots[1]
        if object.getDirection() == "Direction EAST":
            if object.getCordinates()[0] - (data.imageWidth//2) < 45:
                takenSpots[2] = True #not takenSpots[2]
            else:
                takenSpots[2] = False #not takenSpots[2]
        if object.getDirection() == "Direction WEST":
            if (data.width - data.imageHeight//2) - object.getCordinates()[0] < 45:
                takenSpots[3] = True #not takenSpots[3]
            else:
                takenSpots[3] = False #not takenSpots[3]
    for i in range(len(takenSpots)):
        if takenSpots[i] == False:
            if i == 0:
                start = data.spawnPoints[0]
            elif i == 1:
                start = data.spawnPoints[1]
            elif i == 2:
                start = data.spawnPoints[2]
            else:
                start = data.spawnPoints[3]
            destination = (0,0)
            color = random.choice(data.colors)
            newCar = Car(start[0], start[1], data.images[color], color, destination[0],destination[1], start[2])
            data.objects.append(newCar)
            data.spriteObjects.add(newCar)
        else:
            pass
def timerFiredMovement(data):
    for object in data.objects:
        cordinates = object.getCordinates()
        test = object.getDirection()[10:]
        light = lightFacing(data, test.lower())
        if cordinates[0] < 0 or cordinates[0] > data.width or cordinates[1] < 0 or cordinates[1] > data.height:
            data.objects.remove(object)
            object.kill()
            data.score += 1
        if object.getDirection() == "Direction NORTH":
            if object.getCordinates()[1] < light.getPosition()[1]:
                object.moveUp()
            elif light.currentStatus() == True:
                object.moveUp()
            else:
                object.stop()
        if object.getDirection() == "Direction SOUTH":
            if object.getCordinates()[1] > light.getPosition()[1]:
                object.moveDown()
            elif light.currentStatus() == True:
                object.moveDown()
            else:
                object.stop()
        if object.getDirection() == "Direction EAST":
            if object.getCordinates()[0] > light.getPosition()[0]:
                object.moveRight()
            elif light.currentStatus() == True:
                object.moveRight()
            else:
                object.stop()
        if object.getDirection() == "Direction WEST":
            if object.getCordinates()[0] < light.getPosition()[0]:
                object.moveLeft()
            elif light.currentStatus() == True:
                object.moveLeft()
            else:
                object.stop()
        object.updateRect()
        if object.checkCollisions(data.objects):
            data.gameOver = True
            object.stop()
def mousePressed(data, x,y):
    for light in data.trafficLights:
        if light.orientation == "Horizontal":
            attributes = light.getPosition()
            boundsX = attributes[0] + attributes[2]
            boundsY = attributes[1] + attributes[3]
            if attributes[0] < x  < boundsX and attributes[1] < y < boundsY:
                light.changeLight()
        if light.orientation == "Vertical":
            attributes = light.getPosition()
            boundsX = attributes[0] + attributes[3]
            boundsY = attributes[1] + attributes[2]
            if attributes[0] < x  < boundsX and attributes[1] < y < boundsY:
                light.changeLight()
def reDrawAll(data,screen):
    if data.gameMode == "starter":
        starterScreen.redDrawStarterScreen(screen)
    elif data.gameMode == "Game Options":
        gameOptionsScreen.reDrawAllGameOptions(screen)
    elif data.gameMode == "Rules":
        instructionsScreen.reDrawAllInstructions(screen)
def displayRun():
    running = True
    class Struct(object): pass
    data = Struct()
    timer = 0 #seconds
    fps = 100
    animationCycles = 4
    init(data)
    timerFiredNewCharacter(data)
    #data.current = data.objects[0]
    pygame.mixer.music.play(-1, 0.0)
    while running:
        time = clock.tick(fps)
        for event in pygame.event.get():
            if data.gameMode == None:
                continue
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                if data.gameMode == "starter":
                    starterScreen.mouseMotion(*(event.pos))
                if data.gameMode == "Game Options":
                    gameOptionsScreen.mouseMotion(*(event.pos))
                if data.gameMode == "Rules":
                    instructionsScreen.mouseMotion(*(event.pos))
                if data.gameMode == "Level 1":
                    data.gameMode = level1Run()
                if data.gameMode == "Level 2":
                    data.gameMode = level2Run()
                if data.gameMode == "Level 3":
                    data.gameMode = level3Run()
                if data.gameMode == "survival":
                    data.gameMode = survivalRun()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if data.gameMode == "starter":
                    data.gameMode = starterScreen.mousePressed(*(event.pos))
                    break
                if data.gameMode == "Game Options":
                    data.gameMode = gameOptionsScreen.mousePressed(*(event.pos))
                    break
                if data.gameMode == "Rules":
                    data.gameMode = instructionsScreen.mousePressed(*(event.pos))
                    break
                if data.gameMode == "Level 1":
                    data.gameMode = level1Run()
                elif data.gameMode == "Level 2":
                    data.gameMode = level2Run()
                elif data.gameMode == "Level 3":
                    data.gameMode = level3Run()
                elif data.gameMode == "survival":
                    data.gameMode = survivalRun()
            if event.type == pygame.KEYDOWN:
                if data.gameMode == "Rules":
                    data.gameMode = instructionsScreen.keyPressed(event.key)
                    break
        reDrawAll(data, screen)
        pygame.display.update()
    pygame.quit()
def main():
    displayRun()
if __name__ == '__main__':
    main()
