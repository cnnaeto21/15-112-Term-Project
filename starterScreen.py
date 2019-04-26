############################
# starterScreen.py Citation Comment
# All Orginal Code
# Previously cited when I make transparent rectangles
##############################

import module_manager
module_manager.ignore_module('characters.py')
module_manager.ignore_module('display.py')
#module_manager.ignore_module('images')
module_manager.review()
import pygame
pygame.font.get_fonts()
import random
import math
from characters import TrafficLights, Car
#from display import *
import images

pygame.init()
pygame.font.init()
pygame.font.get_fonts()
width = 1290
height = 700
screen = pygame.surface.Surface((width,height))
# screen.fill((0,0,0))
# screen.set_alpha(200)
green = (0,100,0)
red = (255,0,0)
gray = (205,201,201)
class StarterScreen(object):
    def __init__(self, width, height):
        self.margin = 40
        self.width = width
        self.height = height
        self.wordOn = True
        self.greenOn = 50,255,50
        self.greenOff = 0,120,50
        self.redOn = 255,0,0
        self.redOff = 140,0,0
        self.timer = 0
        self.overPlayButton = False
        self.overRulesButtton = False
    def timerFired(self):
        self.timer += 1
        print(self.timer)
        if self.timer % 5 == 0:
            self.on = not self.on
    def mousePressed(self, x,y):
        if self.width//2 - 180 < x < (self.width//2 - 180) + 400 and \
        self.height//2 - 80 < y < (self.height//2 - 80) + 60:
            print("Game Options")
            return "Game Options"
        #(self.width//2 - 180), (self.height//2 - 80), 400, 60)
        if self.width//2 - 180 < x < (self.width//2 - 180) + 400 and \
        self.height//2 + 10 < y < (self.height//2 + 70):
            return "Rules"
        else:
            return "starter"
    def mouseMotion(self, x,y):
        if self.width//2 - 180 < x < (self.width//2 - 180) + 400\
        and self.height//2 - 80 < y < (self.height//2 - 80) + 60:
            self.overPlayButton = True
        #pygame.draw.rect(screen, gray, ((self.width//2 - 180), (self.height//2 + 10), 400, 60)
        elif self.width//2 - 180 < x < (self.width//2 - 180) + 400\
        and self.height//2 + 10 < y < (self.height//2 + 10) + 60:
            self.overRulesButtton = True
        else:
            self.overRulesButtton = False
            self.overPlayButton = False
    def redDrawStarterScreen(self,screen):
        self.timer +=1
        if self.timer % 5 == 0:
            self.wordOn = not self.wordOn
        pygame.draw.rect(screen, (255,255,255), (0,0, width,height))
        pygame.draw.rect(screen, green, (self.margin,self.margin, (width - self.margin*2),(height - self.margin*2)))
        pygame.draw.rect(screen, (0,0,0), (width//2 - 85,0,170, height))
        pygame.draw.rect(screen, (0,0,0), (0,height//2 - 85, width, 170))
        pygame.draw.rect(screen,(255,255,0), (width//2 - 10,0, 10, height))
        pygame.draw.rect(screen, (255,255,0), (width//2 + 10,0, 10, height))
        pygame.draw.rect(screen, (255,255,0), (0,height//2 - 10,width,10))
        pygame.draw.rect(screen, (255,255,0), (0,height//2 + 10 ,width,10))
        pygame.draw.rect(screen, (0,0,0),(width//2 - 65, height//2 -65, 145, 145) )
        surface = pygame.surface.Surface((self.width,self.height))
        surface.fill((0,0,0))
        surface.set_alpha(180)
        screen.blit(surface, (0,0))
        titleFont = pygame.font.SysFont('colonnamtregular', 82)
        titleFont.set_bold(True)
        if self.wordOn:
            redPart = titleFont.render("RED LIGHT",False, self.redOff )
            greenPart = titleFont.render("GREEN LIGHT", False, self.greenOn)
            #self.on = not self.on
        else:
            redPart = titleFont.render("RED LIGHT",False, self.redOn )
            greenPart = titleFont.render("GREEN LIGHT", False, self.greenOff)
        screen.blit(redPart, (self.width//2 - 120, self.height//2 - 180))
        screen.blit(greenPart, (self.width//2 - 180, self.height//2 - 140))
        # Play Button
        pygame.draw.rect(screen, gray, ((self.width//2 - 180), (self.height//2 - 80), 400, 60))
        playFont = pygame.font.SysFont("Verdana", 65)
        if self.overPlayButton:
            play = playFont.render("PLAY", False, (0,0,0))
        else:
            play = playFont.render("PLAY", False, (255,255,255))
        screen.blit(play, (self.width//2 - 30, self.height//2 - 70))


        # Rules Button
        pygame.draw.rect(screen, gray, ((self.width//2 - 180), (self.height//2 + 10), 400, 60))
        rulesFont = pygame.font.SysFont("Verdana", 65)
        if self.overRulesButtton:
            rules = playFont.render("INSTRUCTIONS", False, (0,0,0))
        else:
            rules = playFont.render("INSTRUCTIONS", False, (255,255,255))
        screen.blit(rules, (self.width//2 - 150, self.height//2 + 25))
        # pygame.display.update()
class GameOptions(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.optionsImage = pygame.image.load('images/level 1 Game Board.jpg')
        self.optionsImage = pygame.transform.scale(self.optionsImage, (self.width,self.height))
        self.overLeft = True
        self.overRight = False
        self.opacity = 210
        self.levelsHalf = pygame.surface.Surface((self.width//2,self.height))
        self.levelsHalf.fill((0,0,0))
        self.levelsHalf.set_alpha(self.opacity)
        self.levelsFont = pygame.font.SysFont("lucidahandwritingitalic", 82)
        self.survivalHalf = pygame.surface.Surface((self.width//2,self.height))
        self.survivalHalf.fill((255,255,255))
        self.survivalHalf.set_alpha(self.opacity)
        self.survivalFont = pygame.font.SysFont("lucidahandwritingitalic", 82)
        self.opacity = 180
        self.isOverBackButton = False
        self.backFont = pygame.font.SysFont("arialroundedmtboldregular", 25)
    def mouseMotion(self, x,y):
        if 0 < x < 100 and 0 < y <  60:
            self.isOverBackButton = True
        elif 0 < x < self.width//2:
            self.overLeft = True
            self.overRight = False
            self.isOverBackButton = False
        elif self.width//2 < x < self.width:
            self.overLeft = False
            self.overRight = True
            self.isOverBackButton = False
        else:
            self.isOverBackButton = False
    def mousePressed(self, x,y):
        if 0 < x < 100 and 0 < y <  60:
            return "starter"
        if 0 < x < self.width//2:
            return "Level 1"
        elif self.width//2 < x < self.width:
            return "survival"
    def reDrawAllGameOptions(self, screen):
        screen.blit(self.optionsImage, (0,0))
        screen.blit(self.levelsHalf, (0,0))
        screen.blit(self.survivalHalf, (self.width//2,0))
        if self.overLeft:
            self.levelsFont.set_bold(True)
            self.levels = self.levelsFont.render("LEVELS MODE", False, (255,0,0))
            screen.blit(self.levels, (self.width//2 - 500, self.height//2 - 20))

            self.levels = self.levelsFont.render("SURVIVAL MODE", False, (238,233,233))
            screen.blit(self.levels, (self.width//2 + 50, self.height//2 - 20))
        if self.overRight:
            self.survivalFont.set_bold(True)
            self.survival = self.survivalFont.render("SURVIVAL MODE", False, (0,100,0))
            screen.blit(self.survival, (self.width//2 + 50, self.height//2 - 20))

            self.levels = self.levelsFont.render("LEVELS MODE", False, (0,0,0))
            screen.blit(self.levels, (self.width//2 - 500, self.height//2 - 20))
        if self.isOverBackButton:
            pygame.draw.rect(screen, (0,100,0), (0,0, 100, 60))
            self.home = self.backFont.render("HOME", False, (0,0,0))
            screen.blit(self.home, (15, 20))
        else:
            pygame.draw.rect(screen, (255,0,0), (0,0, 100, 60))
            self.home = self.backFont.render("HOME", False, (0,0,0))
            screen.blit(self.home, (15, 20))
        # pygame.display.update()
class Instructions(object):
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.instructionsImage = pygame.image.load('images/InstructionsBackground.png')
            self.instructionsImage = pygame.transform.scale(self.instructionsImage, (self.width,self.height))
            self.isOverBackButton = False
            self.black = 255,255,255
            self.white = (0,100,0)
            self.backFont = pygame.font.SysFont("arialroundedmtboldregular", 25)
            self.instructionsFont = pygame.font.SysFont("Verdana", 30)
            self.titleFont = pygame.font.SysFont("Arialroundedmtboldregular", 50)
            self.titleFont.set_bold(True)
            self.background = pygame.surface.Surface((self.width,self.height))
            self.background.fill((205,201,201))
            self.background.set_alpha(180)
        def keyPressed(self,key):
            if key == pygame.K_h:
                return 'starter'
        def mouseMotion(self, x,y):
            if 10 < x < 110 and 10 < y <  70:
                self.isOverBackButton = True
            else:
                self.isOverBackButton = False
        def mousePressed(self, x,y):
            if 10 < x < 110 and 10 < y < 70:
                return 'starter'
            else:
                return 'Rules'
        def reDrawAllInstructions(self,screen):
            screen.blit(self.instructionsImage, (0,0))
            screen.blit(self.background, (0,0))

            self.title = self.titleFont.render("INSTRUCTIONS", False, (0,0,0))
            screen.blit(self.title, (self.width//2 - 120, 20))

            self.one = self.instructionsFont.render('1.) Safely Navigate cars to the opposite end of the screen by controlling traffic lights through mouse clicks', False, self.black)
            screen.blit(self.one, (50, 100))

            self.two = self.instructionsFont.render('2.) Navigate the appropriate amount of Cars in the alloted amount of time to complete the respective level', False, self.black)
            screen.blit(self.two,(50, 150))

            self.versions = self.instructionsFont.render("3.) Survive as long as you can in SURVIVAL MODE and complete the three levels in LEVELS MODE", False, self.black)
            screen.blit(self.versions, (20, 200))

            self.three = self.instructionsFont.render('4.) Avoid collisions in the intersections that will result in an automatic GAME OVER', False, self.black)
            screen.blit(self.three,(50, 250))

            self.four = self.instructionsFont.render(" --> Don't leave drivers sitting at red lights for too long or they will take off and risk it all", False, self.black)
            screen.blit(self.four, (50, 300))

            self.goodLuck = self.instructionsFont.render("Now you are ready to control some traffic! Good Luck!!! Hit 'h' or press the home button in the top right corner", \
            False, self.white)
            screen.blit(self.goodLuck, (50, 400))
            if self.isOverBackButton:
                pygame.draw.rect(screen, (0,100,0), (0,0, 100, 60))
                self.home = self.backFont.render("HOME", False, (0,0,0))
                screen.blit(self.home, (15, 20))
            else:
                pygame.draw.rect(screen, (255,0,0), (0,0, 100, 60))
                self.home = self.backFont.render("HOME", False, (0,0,0))
                screen.blit(self.home, (15, 20))
            # pygame.display.update()
class PauseScreen(object):
    def __init__(self,width,height,score,time, level, special = False, minutes = 0):
        self.special = special
        self.minutes = minutes
        self.level = level
        self.width = width
        self.height = height
        self.score = score
        self.time = time
        self.isOverResumeButton = False
        self.isOverRestartButton = False
        self.isOverHomeButton = False
        self.p = pygame.surface.Surface((self.width, self.height))
        self.p.set_alpha(180)
        self.p.fill((255,0,0))
        self.pauseMessageFont = pygame.font.SysFont("Chalkboard SE Light", 76)
        self.scoreFont = pygame.font.SysFont("verdana", 25)
        self.message = self.pauseMessageFont.render("PAUSED", False, (255,255,255))
        self.resumeFont = pygame.font.SysFont("verdana", 56)
    def updateNums(self, score, time, minutes = 0):
        self.score = score
        self.time = time
        self.minutes = minutes
    def mousePressed(self, x,y):
        if self.width//2 - 180 < x < (self.width//2 - 180) + 400\
        and self.height//2 + 50 < y < (self.height//2 + 50) + 80:
            return False
        elif self.width//2 -180 < x < (self.width//2 -180) + 800 \
        and self.height//2 + 150 < y < (self.height//2 + 150) + 80:
            return "Restart"
        elif self.width//2 - 180 < x < (self.width//2 - 180) + 400 \
        and self.height//2 + 250 < y < (self.height//2 + 250) + 80:
            return "starter"
    def mouseMotion(self, x,y):
        if self.width//2 - 180 < x < (self.width//2 - 180) + 400 \
        and self.height//2 + 50 < y < (self.height//2 + 50) + 80:
            self.isOverResumeButton = True
        else:
            self.isOverResumeButton = False
        if self.width//2 -180 < x < (self.width//2 -180) + 800 \
        and self.height//2 + 150 < y < (self.height//2 + 150) + 80:
            self.isOverRestartButton = True
        else:
            self.isOverRestartButton = False
        if self.width//2 - 180 < x < (self.width//2 - 180) + 400 \
        and self.height//2 + 250 < y < (self.height//2 + 250) + 80:
            self.isOverHomeButton = True
        else:
            self.isOverHomeButton = False
    def pauseReDrawAll(self, screen):
        #print("HELLO")
        screen.blit(self.p, (0,0))
        screen.blit(self.message, (self.width//2 - 85, self.height//2 - 150))
        self.scoreMessage = self.scoreFont.render("Score:" + str(self.score), False, (0,0,0))
        if self.special == False:
            self.timeMessage = self.scoreFont.render("Time Remaining: " + str(self.time), False, (0,0,0))
        elif self.special == True:
            self.timeMessage = self.scoreFont.render("Time elapsed = " + \
             str(self.minutes) + ":"+ str(self.time), False, (0,0,0))
        screen.blit(self.scoreMessage, (self.width//2 - 37, self.height//2 -50))
        screen.blit(self.timeMessage, (self.width//2 - 45, self.height//2 - 25))

        pygame.draw.rect(screen, (205,201,201), (self.width//2 - 180, \
            self.height//2 + 50, 400, 80))
        pygame.draw.rect(screen, (205,201,201), (self.width//2 - 180, \
        self.height//2 + 150, 400, 80))

        pygame.draw.rect(screen, (205,201,201), (self.width//2 - 180, \
        self.height//2 + 250, 400, 80))
        if self.isOverResumeButton:
            self.resume = self.resumeFont.render("RESUME", False, (0,100,0))
        elif self.isOverRestartButton:
            self.restart = self.resumeFont.render("RESTART", False, (0,100,0))
        elif self.isOverHomeButton:
            self.home = self.resumeFont.render("HOME", False, (0,100,0))
        else:
            self.resume = self.resumeFont.render("RESUME", False, (0,0,0))
            self.restart = self.resumeFont.render("RESTART", False, (0,0,0))
            self.home = self.resumeFont.render("HOME", False, (0,0,0))
        screen.blit(self.resume, (self.width//2 - 90, self.height//2 + 70))
        screen.blit(self.restart, (self.width//2 - 90, self.height//2 + 180))
        screen.blit(self.home, (self.width//2 - 60, self.height//2 + 270))
        # pygame.display.update()
class WinnerScreen(PauseScreen):
    def __init__(self, width,height, score, time, level):
        super().__init__(width,height, score, time, level)
        self.p = pygame.surface.Surface((self.width, self.height))
        self.p.set_alpha(180)
        self.p.fill((0,110,0))
        self.message = self.pauseMessageFont.render("LEVEL COMPLETED", False, (255,215,0))
        self.isOverNextButton = False
        self.clock = 60
        self.flash = 0

    def mousePressed(self, x,y):
        if self.width//2 - 180 < x < (self.width//2 - 180) + 400\
        and self.height//2 + 50 < y < (self.height//2 + 50) + 80:
            return "Level " + str(self.level)
        elif self.width//2 -180 < x < (self.width//2 -180) + 800 \
        and self.height//2 + 150 < y < (self.height//2 + 150) + 80:
            return "Restart"
        elif self.width//2 - 180 < x < (self.width//2 - 180) + 400 \
        and self.height//2 + 250 < y < (self.height//2 + 250) + 80:
            return "starter"
    def mouseMotion(self, x,y):
        if self.width//2 - 180 < x < (self.width//2 - 180) + 400 \
        and self.height//2 + 50 < y < (self.height//2 + 50) + 80:
            self.isOverNextButton = True
        else:
            self.isOverNextButton = False
        if self.width//2 -180 < x < (self.width//2 -180) + 800 \
        and self.height//2 + 150 < y < (self.height//2 + 150) + 80:
            self.isOverRestartButton = True
        else:
            self.isOverRestartButton = False
        if self.width//2 - 180 < x < (self.width//2 - 180) + 400 \
        and self.height//2 + 250 < y < (self.height//2 + 250) + 80:
            self.isOverHomeButton = True
        else:
            self.isOverHomeButton = False
    def winnerReDrawAll(self, screen):
        #print("HELLO")
        self.flash += 1
        screen.blit(self.p, (0,0))
        if self.flash % 10 == 0:
            self.message = self.pauseMessageFont.render("LEVEL COMPLETED", False, (255,215,0))
        else:
            self.message = self.pauseMessageFont.render("LEVEL COMPLETED", False, (255,165,0))
        screen.blit(self.message, (self.width//2 - 220, self.height//2 - 150))
        self.scoreMessage = self.scoreFont.render("Score:" + str(self.score), False, (0,0,0))
        self.timeMessage = self.scoreFont.render("Time: " + str(self.clock - self.time), False, (0,0,0))
        screen.blit(self.scoreMessage, (self.width//2 - 37, self.height//2 -50))
        screen.blit(self.timeMessage, (self.width//2 - 37, self.height//2 - 25))

        pygame.draw.rect(screen, (205,201,201), (self.width//2 - 180, \
            self.height//2 + 50, 400, 80))
        pygame.draw.rect(screen, (205,201,201), (self.width//2 - 180, \
        self.height//2 + 150, 400, 80))

        pygame.draw.rect(screen, (205,201,201), (self.width//2 - 180, \
        self.height//2 + 250, 400, 80))
        if self.isOverNextButton:
            self.resume = self.resumeFont.render("NEXT LEVEL", False, (0,100,0))
        elif self.isOverRestartButton:
            self.restart = self.resumeFont.render("RESTART", False, (0,100,0))
        elif self.isOverHomeButton:
            self.home = self.resumeFont.render("HOME", False, (0,100,0))
        else:
            self.resume = self.resumeFont.render("NEXT LEVEL", False, (0,0,0))
            self.restart = self.resumeFont.render("RESTART", False, (0,0,0))
            self.home = self.resumeFont.render("HOME", False, (0,0,0))
        screen.blit(self.resume, (self.width//2 - 90, self.height//2 + 70))
        screen.blit(self.restart, (self.width//2 - 90, self.height//2 + 180))
        screen.blit(self.home, (self.width//2 - 60, self.height//2 + 270))
        # pygame.display.update()
class CompletedScreen(WinnerScreen):
    def __init__(self,width, height, score, time, level):
        super().__init__(width, height,score,time,level)
        self.pauseMessageFont = pygame.font.SysFont("verdana", 76)
        self.pauseMessageFont.set_bold(True)
    def mousePressed(self, x,y):
        if self.width//2 - 180 < x < (self.width//2 - 180) + 400\
        and self.height//2 + 50 < y < (self.height//2 + 50) + 80:
            return "starter"

        elif self.width//2 - 210 < x < (self.width//2 -180) + 450 \
        and self.height//2 + 150 < y < (self.height//2 + 150) + 80:
            return "survival"
        else:
            return "Level 3"
    def mouseMotion(self, x,y):
        if self.width//2 - 180 < x < (self.width//2 - 180) + 400 \
        and self.height//2 + 50 < y < (self.height//2 + 50) + 80:
            self.isOverNextButton = True
        else:
            self.isOverNextButton = False
        if self.width//2 - 210 < x < (self.width//2 - 180) + 450 \
        and self.height//2 + 150 < y < (self.height//2 + 150) + 80:
            self.isOverRestartButton = True
        else:
            self.isOverRestartButton = False
    def reDrawAllCompletedScreen(self, screen):
        self.p = pygame.surface.Surface((self.width, self.height))
        self.p.set_alpha(180)
        self.p.fill((0,110,0))
        screen.blit(self.p, (0,0))
        self.message = self.pauseMessageFont.render("GAME COMPLETED", False, (255,215,0))
        screen.blit(self.message, (self.width//2 - 250, self.height//2 - 150))
        pygame.draw.rect(screen, (205,201,201), (self.width//2 - 180, \
            self.height//2 + 50, 400, 80))
        self.playFont = pygame.font.SysFont("verdana", 65)
        if self.isOverNextButton:
            self.play = self.playFont.render("HOME", False, (0,100,0))
        else:
            self.play = self.playFont.render("HOME", False, (255,255,255))
        screen.blit(self.play, (self.width//2 - 90, self.height//2 + 70))

        pygame.draw.rect(screen, (205,201,201), (self.width//2 - 210, \
        self.height//2 + 150, 450, 80))
        self.resumeFont = pygame.font.SysFont("verdana", 65)
        if self.isOverRestartButton:
            self.restart = self.resumeFont.render("SURVIVAL MODE", False, (0,100,0))
        else:
            self.restart = self.resumeFont.render("SURVIVAL MODE", False, (255,255,255))
        screen.blit(self.restart, (self.width//2 - 155, self.height//2 + 170))
