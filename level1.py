################
# level1.py CITATION
# lines 14 - 272 Orginal code
# lines 273 - 275 taken from stackoverflow link below
# https://stackoverflow.com/questions/6339057/draw-a-transparent-rectangle-in-pygame
# Rest Orginal code, run Structutre from Lukas Pereze 15112 pygame blog
##################






import module_manager
# module_manager.ignore_module('starterScreen.py')
module_manager.ignore_module('display.py')
module_manager.ignore_module('characters.py')
module_manager.review()
import pygame
import random
import math
from characters import TrafficLights, Car
from display import *
from starterScreen import PauseScreen, WinnerScreen
# from level2 import *
#from levels import level1Board
import images

pygame.init()
pygame.font.init()
pygame.font.get_fonts()
####################################
fps = 100
width = 1280
height = 700
green = (0,100,0)
red = (255,0,0)
black = (0,0,0)
beige = (250,250,210)
clock = pygame.time.Clock()
def init(data):
    data.done = False
    data.outtaTime = False
    data.collision = False
    data.scoreFont = pygame.font.SysFont("Verdana", 25)
    data.pauseFont = pygame.font.SysFont("Verdana", 56)
    data.resumeFont = pygame.font.SysFont("Verdana", 35)
    data.gameOverFont = pygame.font.SysFont("Bauhaus 93", 56)
    data.gameOverFont.set_bold(True)
    data.idleTime = 160
    data.stop = False
    data.score = 0
    data.timeLeft = 50
    data.gameOver = False
    data.isPaused = False
    data.gameMode = "starter"
    data.margin = 40
    data.imageWidth = 30
    data.imageHeight = 50
    data.goal = 10
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
    data.pauseScreen = PauseScreen(data.width, data.height, data.score, data.timeLeft,2)
    data.winnerScreen = WinnerScreen(data.width,data.height, data.score, data.timeLeft,2)
    data.isComplete = False
def lightFacing(data, direction):
    for light in data.trafficLights:
        if light.whatCardinal() == direction:
            return light
def timerFiredNewCharacter(data):
    takenSpots = [False,False,False,False]
    for object in data.objects:
        if object.getDirection() == "Direction NORTH":
            if (data.height - data.imageHeight//2) - object.getCordinates()[1] < 65:
                takenSpots[0] = True #not takenSpots[0]
            else:
                takenSpots[0] = False # not takenSpots[0]
        if object.getDirection() == "Direction SOUTH":
            if object.getCordinates()[1] - (data.imageHeight - 25) < 65:
                takenSpots[1] = True # not takenSpots[1]
            else:
                takenSpots[1] = False #not takenSpots[1]
        if object.getDirection() == "Direction EAST":
            if object.getCordinates()[0] - (data.imageWidth//2) < 55:
                takenSpots[2] = True #not takenSpots[2]
            else:
                takenSpots[2] = False #not takenSpots[2]
        if object.getDirection() == "Direction WEST":
            if (data.width - data.imageHeight//2) - object.getCordinates()[0] < 55:
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
    if data.timeLeft == 0 and data.score < 10:
        data.gameOver = True
        data.outtaTime = True
        #return "Done"
    if data.score >= 10 and data.timeLeft > 0:
        data.winnerScreen.updateNums(data.score,data.timeLeft)
        data.isComplete = True
        data.gameOver = True
        data.done = True
    for object in data.objects:
        cordinates = object.getCordinates()
        test = object.getDirection()[10:]
        light = lightFacing(data, test.lower())
        if cordinates[0] < 0 or cordinates[0] > data.width or cordinates[1] < 0\
        or cordinates[1] > data.height:
            data.objects.remove(object)
            object.kill()
            data.score += 1
        if object.getDirection() == "Direction NORTH":
            if object.idle() > data.idleTime:
                object.moveUp()
            if object.getCordinates()[1] < light.getPosition()[1]:
                object.moveUp()
            elif light.currentStatus() == True:
                object.moveUp()
                object.timeStopped = 0
            else:
                object.stop()
                object.addTime()
        if object.getDirection() == "Direction SOUTH":
            if object.idle() > data.idleTime:
                object.moveDown()
            if object.getCordinates()[1] > light.getPosition()[1]:
                object.moveDown()
            elif light.currentStatus() == True:
                object.moveDown()
                object.timeStopped = 0
            else:
                object.stop()
                object.addTime()
        if object.getDirection() == "Direction EAST":
            if object.idle() > data.idleTime:
                object.moveRight()
            if object.getCordinates()[0] > light.getPosition()[0]:
                object.moveRight()
            elif light.currentStatus() == True:
                object.moveRight()
                object.timeStopped = 0
            else:
                object.stop()
                object.addTime()
        if object.getDirection() == "Direction WEST":
            if object.idle() > data.idleTime:
                object.moveLeft()
            if object.getCordinates()[0] < light.getPosition()[0]:
                object.moveLeft()
            elif light.currentStatus() == True:
                object.moveLeft()
                object.timeStopped = 0
            else:
                object.stop()
                object.addTime()
        object.updateRect()
        if object.checkCollisions(data.objects):
            data.gameOver = True
            object.stop()
            data.collision = True
def mousePressed(data, x,y):
    if 130 < x < 210  and 5 < y < 30:
        data.isPaused = True
        data.gameOver = True
        print(data.isPaused)
        print(data.gameOver)
        return False
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
def keyPressed(data, key):
    print(data.done)
    if data.gameOver == True:
        if key == pygame.K_h:
            #displayRun()
            return "starter"
        elif key == pygame.K_r:
            #init(data)
            return "Level 1"
        else:
            return "Level 1"
    if data.isPaused == True:
        data.pauseScreen.keyPressed()
        return 'Level 1'
    else:
        pass
def reDrawAllLevel1(data,screen):
    test = pygame.surface.Surface((data.width,data.height))
    test.fill((255,255,255))
    pygame.draw.rect(screen, (65,105,225), (0,0, width,height))
    pygame.draw.rect(screen, green, (data.margin,data.margin, (width - data.margin*2),(height - data.margin*2)))
    pygame.draw.rect(screen, (0,0,0), (width//2 - 85,0,170, height))
    pygame.draw.rect(screen, (0,0,0), (0,height//2 - 85, width, 170))
    pygame.draw.rect(screen,(255,255,0), (width//2 - 10,0, 10, height))
    pygame.draw.rect(screen, (255,255,0), (width//2 + 10,0, 10, height))
    pygame.draw.rect(screen, (255,255,0), (0,height//2 - 10,width,10))
    pygame.draw.rect(screen, (255,255,0), (0,height//2 + 10 ,width,10))
    pygame.draw.rect(screen, (0,0,0),(width//2 - 65, height//2 -65, 145, 145) )
    score = data.scoreFont.render("Score: " + str(data.score), False, (0,0,0))
    time = data.scoreFont.render("Time: " +  str(data.timeLeft) + " secs", False, (0,0,0))
    cars = data.scoreFont.render("Cars Remaing " + str(data.goal - data.score), False, (0,0,0))
    screen.blit(cars, (900, 5))
    levelName = data.scoreFont.render("LEVEL 1", False, (0,0,0))
    screen.blit(levelName, (300, 5))
    screen.blit(time, (data.width - 110, 5))
    pygame.draw.rect(screen, (0,0,0), (130, 5, 80, 25))
    pygame.draw.rect(screen, (255,255,255), (135, 9, 70, 15))
    pauseButton = data.scoreFont.render("PAUSE", False, (0,0,0))
    screen.blit(pauseButton, (140, 8))
    for object in data.objects:
        facing = object.getDirection
        object.drawMe(screen, facing)
    for light in data.trafficLights:
        light.drawLight(screen)
    if data.gameOver == False and data.isComplete == False:
        screen.blit(score, (5 ,5))
    if data.gameOver == True and data.isPaused == False and data.isComplete == False:
        s = pygame.Surface((data.width,data.height))  # the size of your rect
        s.set_alpha(128)                # alpha level
        s.fill((255,255,255))           # this fills the entire surface
        screen.blit(s, (0,0))
        pygame.draw.rect(screen,(205,201,201), (data.width//2 - 220, data.height//2 - 300, 500, 200))
        if data.collision:
            reason = data.scoreFont.render("Uh Oh. A collision Occured!", False, (0,0,0))
            screen.blit(reason, (data.width//2 - 100, data.height//2 - 290))
        if data.outtaTime:
            reason = data.scoreFont.render("Too Slow. You ran outta time :/", False, (0,0,0))
            screen.blit(reason, (data.width//2 - 100, data.height//2 - 290))
        message = data.gameOverFont.render("GAME OVER :(", False, (255,0,0))
        screen.blit(message, (data.width//2 - 140, data.height//2 - 270))
        screen.blit(score, (data.width//2 - 25, data.height//2 - 215))
        restart = data.scoreFont.render("Press the 'r' key to restart OR the 'h' key to go home", False, (0,0,0))
        screen.blit(restart, (data.width//2 - 160, data.height //2 - 180))
    if data.isPaused == True and data.gameOver == True:
        data.pauseScreen.pauseReDrawAll(screen)
    if data.isComplete and data.gameOver == True:
        data.winnerScreen.winnerReDrawAll(screen)
def level1Run():
    running = True
    class Struct(object): pass
    data = Struct()
    timer = 0 #seconds
    fps = 50
    init(data)
    timerFiredNewCharacter(data)
    data.current = data.objects[0]
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    while running:
        time = clock.tick(fps)
        if data.isComplete == True and data.gameOver == True:
            #timerFiredMovement(data)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    choice = data.winnerScreen.mousePressed(*(event.pos))
                    print(choice)
                    if choice == "Level 2":
                        data.done = True
                        return "Level 2"
                    if choice == "Restart":
                        init(data)
                        return "Level 1"
                    if choice == "starter":
                        return "starter"
                if event.type == pygame.MOUSEMOTION:
                    data.winnerScreen.mouseMotion(*(event.pos))
                if event.type == pygame.KEYDOWN:
                    pass
        if data.gameOver == False and data.isPaused == False:
            if pygame.time.get_ticks() % 100 == 0:
                data.timeLeft -= 1
            timer += 1
            if timer % 100 == 0:
                timerFiredNewCharacter(data)
            timerFiredMovement(data)
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    data.timeLeft -= 1
                if event.type == pygame.QUIT:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePressed(data, *event.pos)
                    break
        elif data.isPaused == True and data.gameOver == True:
             data.pauseScreen.updateNums(data.score,data.timeLeft)
             for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                      running = False
                 if event.type == pygame.MOUSEBUTTONDOWN:
                     if data.pauseScreen.mousePressed(*(event.pos)) == False:
                         data.isPaused = False
                         data.gameOver = False
                         break
                         #return "Level 1"
                     if data.pauseScreen.mousePressed(*(event.pos)) == "Restart":
                        init(data)
                        return "Level 1"
                     if data.pauseScreen.mousePressed(*(event.pos)) == "starter":
                        return "starter"
                 if event.type == pygame.MOUSEMOTION:
                    data.pauseScreen.mouseMotion(*(event.pos))
        elif data.isPaused == False and data.gameOver == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     running = False
                if event.type == pygame.KEYDOWN:
                    response = keyPressed(data, event.key)
                    if response == "Level 1":
                        init(data)
                        return response
                    else:
                        return response
        else:
            print("HELLLOOOOO")
        reDrawAllLevel1(data, screen)
        pygame.display.update()
    pygame.quit()
