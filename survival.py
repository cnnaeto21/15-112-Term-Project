#############################
#Survival.py citation Comment
# lines 6- 293 Orginal code
# lines 294 - 297 code taken from stackoverflow link below
# # https://stackoverflow.com/questions/6339057/draw-a-transparent-rectangle-in-pygame
# lines 300 - 325 Original Code
# line 326 and 356 code taken from stackoverflow link below
# https://stackoverflow.com/questions/30720665/countdown-timer-in-pygame
# rest Original Code
##########################TREYWAY###
import module_manager
module_manager.ignore_module('starterScreen.py')
module_manager.ignore_module('display.py')
module_manager.ignore_module('characters.py')
module_manager.review()
import pygame
import random
import math
from characters import TrafficLights, Car
from display import *
from starterScreen import PauseScreen, WinnerScreen
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
#data.scoreFont = pygame.font.SysFont("Verdana", 25)
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
def init(data):
    data.outtaTime = False
    data.collision = False
    data.scoreFont = pygame.font.SysFont("verdana", 25)
    data.pauseFont = pygame.font.SysFont("verdana", 56)
    data.resumeFont = pygame.font.SysFont("verdana", 35)
    data.gameOverFont = pygame.font.SysFont("bauhaus93", 56)
    data.gameOverFont.set_bold(True)
    data.idleTime = 160
    data.stop = False
    data.score = 0
    data.timeLeft = 70
    data.gameOver = False
    data.isPaused = False
    data.gameMode = "starter"
    data.margin = 40
    data.imageWidth = 30
    data.imageHeight = 50
    data.seconds = 00
    data.minutes = 0
    data.goal = 30
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
    data.pauseScreen = PauseScreen(data.width, data.height, data.score, data.seconds, 3, True, data.minutes)
    data.finishedScreen = CompletedScreen(data.width,data.height, data.score, data.timeLeft, 3)
    data.isComplete = False
def timerFired(data):
    data.seconds += 1
    if data.seconds == 59:
        data.seconds = 00
        data.minutes += 1
def lightFacing(data, direction):
    for light in data.trafficLights:
        if light.whatCardinal() == direction:
            return light
def timerFiredNewCharacter(data):
    takenSpots = [False,False,False,False]
    for object in data.objects:
        if object.getDirection() == "Direction NORTH":
            if (data.height - data.imageHeight) - object.getCordinates()[1] < 45:
                takenSpots[0] = True #not takenSpots[0]
            else:
                takenSpots[0] = False # not takenSpots[0]
        if object.getDirection() == "Direction SOUTH":
            if object.getCordinates()[1] - (data.imageHeight) < 45:
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
    # if data.timeLeft == 0 and data.score < 30:
    #     data.gameOver = True
    #     data.outtaTime = True
    # if data.score >= 30 and data.timeLeft > 0:
    #     #data.winnerScreen.updateNums(data.score,data.timeLeft)
    #     data.isComplete = True
    #     data.gameOver = True
    # data.timer += 1
    # if data.timer % 100 == 0:
    #     data.seconds += 1
    # if data.seconds == 59:
    #     data.seconds = 00
    #     data.minutes += 1
     for object in data.objects:
        cordinates = object.getCordinates()
        test = object.getDirection()[10:]
        light = lightFacing(data, test.lower())
        if cordinates[0] < 0 or cordinates[0] > data.width or cordinates[1] < 0\
        or cordinates[1] > data.height:
            #data.current = data.objects[0]
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
    # for i in range(len(data.objects)):
    #     pos = data.objects[i].getCordinates()
    #     dimensions = data.objects[i].getDimensions()
    #     boundsX = pos[0] + dimensions[0]
    #     boundsY = pos[1] + dimensions[1]
    #     if pos[0] < x < boundsX and pos[1] < y < boundsY:
    #         return i
    if 130 < x < 210  and 5 < y < 30:
        # print("YUH")
        data.isPaused = True
        data.gameOver = True
        # print(data.isPaused)
        # print(data.gameOver)
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
    if data.gameOver == True:
        if key == pygame.K_h:
            #displayRun()
            return "starter"
        elif key == pygame.K_r:
            # print("BOI")
            #init(data)
            return "survival"
        else:
            return "survival"
    # elif data.gameOver == False:
    #     if key == pygame.K_p:
    #         data.isPaused = not data.isPaused
    #         data.gameOver = True
    #         return 'paused'
    if data.isPaused == True:
        data.pauseScreen.keyPressed()
        return 'survival'
def reDrawAllSurvival(data,screen):
    #print("Level 3 Check")
    # test = pygame.surface.Surface((data.width,data.height))
    # test.fill((255,255,255))
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
    time = data.scoreFont.render("Time elapsed = " + str(data.minutes) + ":" + str(data.seconds), False, (0,0,0))
    #cars = data.scoreFont.render("Cars Remaing " + str(data.goal - data.score), False, (0,0,0))
    #screen.blit(cars, (900, 5))
    levelName = data.scoreFont.render("SURVIVAL", False, (0,0,0))
    screen.blit(levelName, (300, 5))
    screen.blit(time, (data.width - 160, 5))
    pygame.draw.rect(screen, (0,0,0), (130, 5, 80, 25))
    pygame.draw.rect(screen, (255,255,255), (135, 9, 70, 15))
    pauseButton = data.scoreFont.render("PAUSE", False, (0,0,0))
    screen.blit(pauseButton, (140, 8))
    for object in data.objects:
        #print(object)
        #print(object.getPositionX, object.getPositionY)
        facing = object.getDirection
        object.drawMe(screen, facing)
    for light in data.trafficLights:
        # print("Scary Hours")
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
        screen.blit(time, (data.width//2 - 55, data.height//2 - 235))
        restart = data.scoreFont.render("Press the 'r' key to restart OR the 'h' key to go home", False, (0,0,0))
        screen.blit(restart, (data.width//2 - 160, data.height //2 - 180))
    if data.isPaused == True and data.gameOver == True:
        data.pauseScreen.updateNums(data.score,data.seconds,data.minutes)
        data.pauseScreen.pauseReDrawAll(screen)
    if data.isComplete == True and data.gameOver == True:
        data.finishedScreen.reDrawAllCompletedScreen(screen)
def survivalRun():
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
                    choice = data.finishedScreen.mousePressed(*(event.pos))
                    if choice == "starter":
                        return "starter"
                    if choice == "Restart":
                        init(data)
                        return "Level 3"
                    if choice == "Survival Mode":
                        return "survival"
                if event.type == pygame.MOUSEMOTION:
                    data.finishedScreen.mouseMotion(*(event.pos))
                if event.type == pygame.KEYDOWN:
                    pass
        if data.gameOver == False and data.isPaused == False:
            timer += 1
            if timer % 100 == 0:
                timerFiredNewCharacter(data)
            timerFiredMovement(data)
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    timerFired(data)
                if event.type == pygame.QUIT:
                     running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePressed(data, *event.pos)
                    break
                if event.type == pygame.KEYDOWN:
                     return keyPressed(data, event.key)
                     #break
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
                        return "survival"
                     if data.pauseScreen.mousePressed(*(event.pos)) == "starter":
                        return "starter"
                 if event.type == pygame.MOUSEMOTION:
                    data.pauseScreen.mouseMotion(*(event.pos))
        elif data.isPaused == False and data.gameOver == True:
            # print("Steady")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     running = False
                if event.type == pygame.KEYDOWN:
                    response = keyPressed(data, event.key)
                    if response == "survival":
                        init(data)
                    return response
        reDrawAllSurvival(data, screen)
        pygame.display.update()
    pygame.quit()
