#########################################
# File Name: fisherMann.py
# Description: ISU computer science game
# Author: Jennifer
# Date: 05/29/2018
#########################################
from math import sin,cos,pi
from math import sqrt
from random import randint
import pygame
pygame.init()
WIDTH = 800
HEIGHT= 600
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))

TOP    = 0  
BOTTOM = HEIGHT
LEFT   = 0     
RIGHT  = WIDTH

#colors
GREEN = (  0,255,  0)
BLUE  = (  0,  0,128)
WHITE = (255,255,255)
BLACK = (  0,  0,  0)
RED   = (255,  0,  0)
YELLOW = (125,  0,  0)
PURPLE = (125,  0,125)
LIGHTBLUE = ( 84,193,255)
LIGHTERBLUE = (189,231,255)

#drawshape
outline = 0

#fonts
FONT = pygame.font.SysFont("Arial Black",18)
FONT_RULE = pygame.font.SysFont("Arial Black",14)
FONT_TITLE = pygame.font.SysFont("Broadway",64)

#pictures
#opening logo
openingPic = pygame.image.load("opening.png")
#fish picture & get dimensions
fishPic = pygame.image.load("fish4.png")
fishRect = fishPic.get_rect()
fishW = fishRect.width
fishH = fishRect.height
#seahorse picture & get dimensions
seahorsePic = pygame.image.load("seahorse4.png")
seahorseRect = seahorsePic.get_rect()
seahorseW = seahorseRect.width
seahorseH = seahorseRect.height
#pearl shell picture
shellPic = pygame.image.load("shell3.png")
#lightning fish picture
lightPic = pygame.image.load("light4.png")
#crab picture & get dimensions
crabPic = pygame.image.load("crab4.png")
crabRect = crabPic.get_rect()
crabW = crabRect.width
crabH = crabRect.height

#Pictures for the avatar page
#items to be put on avatar
hat1 = pygame.image.load("hat1.png")
hat2 = pygame.image.load("hat2.png")
hat3 = pygame.image.load("hat3.png")
neck1 = pygame.image.load("neck1.png")
neck2 = pygame.image.load("neck2.png")
neck3 = pygame.image.load("neck3.png")
shoe1 = pygame.image.load("shoe1.png")
shoe2 = pygame.image.load("shoe2.png")
shoe3 = pygame.image.load("shoe3.png")
hand1 = pygame.image.load("hand1.png")
hand2 = pygame.image.load("hand2.png")
hand3 = pygame.image.load("hand3.png")

#readjusted pictures (smaller in size to fit in "closet")
neck2_2 = pygame.image.load("neck2_2.png")

shoe1_2 = pygame.image.load("shoe1_2.png")
shoe2_2 = pygame.image.load("shoe2_2.png")
shoe3_2 = pygame.image.load("shoe3_2.png")

hand1_2 = pygame.image.load("hand1_2.png")
hand2_2 = pygame.image.load("hand2_2.png")
hand3_2 = pygame.image.load("hand3_2.png")

#lists of the different items to be displayed on avatar screen
hats = [hat1,hat2,hat3]
necks = [neck1,neck2,neck3]
shoes = [shoe1,shoe2_2,shoe3_2]
hands = [hand1,hand2,hand3]

#readjusted for game screen
hat1_3 = pygame.image.load("hat1_3.png")
hat2_3 = pygame.image.load("hat2_3.png")
hat3_3 = pygame.image.load("hat3_3.png")
shoe1_3 = pygame.image.load("shoe1_3.png")
shoe2_3 = pygame.image.load("shoe2_3.png")
shoe3_3 = pygame.image.load("shoe3_3.png")
neck1_3 = pygame.image.load("neck1_3.png")
neck2_3 = pygame.image.load("neck2_3.png")
neck3_3 = pygame.image.load("neck3_3.png")

#lists of the different items to be displayed on game screen
hats_display = [hat1_3,hat2_3,hat3_3]
necks_display = [neck1_3,neck2_3,neck3_3]
shoes_display = [shoe1_3,shoe2_3,shoe3_3]
hands_display = [hand1_2,hand2_2,hand3_2]

#---------------------------------------#
# functions                             #
#---------------------------------------#

#drawing the first the opening page
def drawOpeningScreen():
    gameWindow.fill(LIGHTBLUE)
    gameWindow.blit(openingPic,(40,40))
    pygame.draw.rect(gameWindow, LIGHTERBLUE, (225,550,350,30), 0)
    pygame.draw.rect(gameWindow, WHITE, (225,550,350,30), 5)
    pressRight = FONT.render("Press RIGHT to continue",2,WHITE)
    gameWindow.blit(pressRight,(270,550))
    pygame.display.update()

#drawing the rules page
def drawRulesScreen():
    gameWindow.fill(LIGHTBLUE)
    opening = FONT_TITLE.render("Rules",2,WHITE)
    gameWindow.blit(opening,(300,40))
    pygame.draw.rect(gameWindow, LIGHTERBLUE, (225,550,350,30), 0)
    pygame.draw.rect(gameWindow, WHITE, (225,550,350,30), 5)
    pressSpace = FONT.render("Press RIGHT to start",2,WHITE)
    gameWindow.blit(pressSpace,(270,550))
    
    #general description
    rule1 = FONT.render("During the game, press SPACE to let down the hook",2,WHITE)
    gameWindow.blit(rule1,(100,150))
    rule2 = FONT.render("Get as many points without losing lives",2,WHITE)
    gameWindow.blit(rule2,(100,180))
    rule3 = FONT.render("If the hook touches:",2,WHITE)
    gameWindow.blit(rule3,(100,210))

    #rules for each of the fish/sea animal
    fishRule = FONT_RULE.render("Fish -> one point",2,WHITE)
    gameWindow.blit(fishRule,(100,260))
    horseRule = FONT_RULE.render("Seahorse -> ten seconds time boost",2,WHITE)
    gameWindow.blit(horseRule,(100,310))
    crabRule = FONT_RULE.render("Crab -> five points, lose one life",2,WHITE)
    gameWindow.blit(crabRule,(100,360))
    lightRule = FONT_RULE.render("Lightning Fish -> ten points, lose one life & shocks other fish",2,WHITE)
    gameWindow.blit(lightRule,(100,410))
    shellRule = FONT_RULE.render("Shell -> twenty to forty points depending",2,WHITE)
    gameWindow.blit(shellRule,(100,460))

    #put the picture of the corresponding picture beside its description
    gameWindow.blit(fishPic,(700,240))
    gameWindow.blit(seahorsePic,(700,290))
    gameWindow.blit(crabPic,(700,360))
    gameWindow.blit(lightPic,(700,410))
    gameWindow.blit(shellPic,(670,460)) 
    pygame.display.update()

#drawing the items on the stickman when the user clicks on it
def drawCharacter():
    if drawHat == True:
        gameWindow.blit(hats[hatNum],(140,100))
    if drawNeck == True:
        gameWindow.blit(necks[neckNum],(175,260))
    if drawShoe == True:
        gameWindow.blit(shoes[shoeNum],(100,450))
    if drawHand == True:
        gameWindow.blit(hands[handNum],(270,250))

#drawing the avatar screen
def drawAvatarScreen():
    gameWindow.fill(LIGHTBLUE)

    avatar = FONT_TITLE.render("Avatar",2,WHITE)
    gameWindow.blit(avatar,(300,40))
    
    pygame.draw.rect(gameWindow, LIGHTERBLUE, (225,550,350,30), 0)
    pygame.draw.rect(gameWindow, WHITE, (225,550,350,30), 5)
    pressRight = FONT.render("Press RIGHT to continue",2,WHITE)
    gameWindow.blit(pressRight,(270,550))

    #drawing the closet
    pygame.draw.rect(gameWindow, LIGHTERBLUE, (350,120,420,390), 0)
    pygame.draw.rect(gameWindow, WHITE, (350,120,420,390), 5)
    pygame.draw.line(gameWindow,WHITE,(350,227),(770,227),3)
    pygame.draw.line(gameWindow,WHITE,(350,317),(770,317),3)
    pygame.draw.line(gameWindow,WHITE,(350,407),(770,407),3)
    pygame.draw.line(gameWindow,WHITE,(350+140,120),(350+140,510),3)
    pygame.draw.line(gameWindow,WHITE,(350+280,120),(350+280,510),3)

    #stickman
    #head
    pygame.draw.circle(gameWindow, WHITE, (200, 200), 50, 0)
    pygame.draw.circle(gameWindow, BLACK, (200, 200), 50, 3)
    #arms
    pygame.draw.line(gameWindow,BLACK,(100,330),(200,300),3)
    pygame.draw.line(gameWindow,BLACK,(200,300),(300,300),3)
    #body
    pygame.draw.line(gameWindow,BLACK,(200,250),(200,400),3)
    #legs
    pygame.draw.line(gameWindow,BLACK,(200,400),(170,470),3)
    pygame.draw.line(gameWindow,BLACK,(200,400),(230,470),3)
    #stick/fishing rod
    if drawHand == False:
        pygame.draw.line(gameWindow,BLACK,(300,200),(300,470),3)

    #the items on the closet
    gameWindow.blit(hat1,(360,130))
    gameWindow.blit(hat2,(500,130))
    gameWindow.blit(hat3,(640,110))
    gameWindow.blit(neck1,(410,245))
    gameWindow.blit(neck2_2,(550,235))
    gameWindow.blit(neck3,(660,235))
    gameWindow.blit(shoe1_2,(360,370))
    gameWindow.blit(shoe2_2,(470,330))
    gameWindow.blit(shoe3_2,(600,330))
    gameWindow.blit(hand1_2,(420,420))
    gameWindow.blit(hand2_2,(550,420))
    gameWindow.blit(hand3_2,(680,420))

    #draw the user selected items on the stickman
    drawCharacter()
    pygame.display.update()
    
#distance for collision
def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

#drawing fish
def drawFish():
    for i in range(len(fishX)):
        if fishDraw[i]==True:
            #rectangle to see collision
            #pygame.draw.rect(gameWindow, BLUE, (fishX[i],fishY[i],fishW,fishH), 1)
            gameWindow.blit(fishPic,(fishX[i],fishY[i]))
            
#drawing crab
def drawCrab():
    for i in range(len(crabX)):
        if crabDraw[i]==True:
            #rectangle to see collision
            #pygame.draw.rect(gameWindow, YELLOW, (crabX[i],crabY[i],crabW,crabH), 1)
            gameWindow.blit(crabPic,(crabX[i],crabY[i]))
            
#drawing seahorse
def drawSeahorse():
    for i in range(len(seaHorseX)):
        if seaHorseDraw[i]==True:
            #rectangle to see collision
            #pygame.draw.rect(gameWindow, RED, (seaHorseX[i],seaHorseY[i],seahorseW,seahorseH), 1)
            gameWindow.blit(seahorsePic,(seaHorseX[i],seaHorseY[i]))
            
#drawing shells
def drawShell():
    for i in range(len(shellX)):
        if shellDraw[i]==True:
            #the circle to see collision
            #pygame.draw.circle(gameWindow, PURPLE, (shellX[i], shellY[i]), shellR[i], outline)
            gameWindow.blit(shellPic,(shellX[i]-shellRadius,shellY[i]-shellRadius))
            
#drawing lightning fish
def drawLightningfish():
    for i in range(len(lightX)):
        if lightDraw[i]==True:
            #the circle to see collision
            #pygame.draw.circle(gameWindow, GREEN, (lightX[i], lightY[i]), lightR[i], outline)
            gameWindow.blit(lightPic,(lightX[i]-lightRadius,lightY[i]-lightRadius))
            
#drawing the fish hook
def drawVectorAndLine():
    if drawVector ==True:
        #normal black fishing rod swinging
        pygame.draw.line(gameWindow,BLACK,(CENTERX,CENTERY),(CENTERX+vectorX,CENTERY+vectorY),1)
        pygame.draw.line(gameWindow,BLACK,(CENTERX,CENTERY),(CENTERX+VECTOR,CENTERY),1)
    if drawLine == True:
        #the rod turn red when letting down
        pygame.draw.line(gameWindow,RED,(CENTERX,CENTERY),(objectX,objectY),2)

#drawing the number of lives
def drawLives():
    spaceBetweenLives = 30
    defaultLives = 3
    #the current number of lives
    for i in range (numberLives):
        pygame.draw.circle(gameWindow, RED, (100+i*spaceBetweenLives, 30), 10, outline)
    #the number of lives to begin with
    for i in range (defaultLives):
        pygame.draw.circle(gameWindow, BLACK, (100+i*spaceBetweenLives, 30), 10, 3)

#drawing the count down timer
def drawTimer():
    countDown = FONT.render("Time left: " + str(timeLeft),1,BLACK)
    gameWindow.blit(countDown,(160,50))

#drawing the points counter
def drawCounter():
    pointsDisplay = FONT.render(str(points),1,BLACK)
    gameWindow.blit(pointsDisplay,(160,70))

#drawing the menu/pause button
def drawMenuButton():
    pygame.draw.rect(gameWindow, LIGHTBLUE, (650,30,100,50), 0)
    pygame.draw.rect(gameWindow, WHITE, (650,30,100,50), 5)
    menuButton = FONT.render("MENU",2,WHITE)
    gameWindow.blit(menuButton,(670,40))

#drawing the menu screen once pressed the menu button
def drawMenu():
    pygame.draw.rect(gameWindow, LIGHTBLUE, (100,100,600,400), 0)
    pygame.draw.rect(gameWindow, WHITE, (100,100,600,400), 5)
    menu = FONT_TITLE.render("MENU",2,WHITE)
    gameWindow.blit(menu,(300,150))
    #return back to game button
    pygame.draw.rect(gameWindow, LIGHTERBLUE, (200,420,400,30), 0)
    pygame.draw.rect(gameWindow, WHITE, (200,420,400,30), 5)
    returnBack = FONT.render("Return back to game",2,WHITE)
    gameWindow.blit(returnBack,(300,420))
    
    pygame.display.update()

#drawing the proceed to next level button beside menu button
def drawNextLevelButton():
    pygame.draw.rect(gameWindow, LIGHTBLUE, (500,30,100,50), 0)
    pygame.draw.rect(gameWindow, WHITE, (500,30,100,50), 5)
    menuButton = FONT_RULE.render("Next Level",2,WHITE)
    gameWindow.blit(menuButton,(505,40))

#drawing the character in the game screen
def drawGameCharacter():
    #head
    pygame.draw.circle(gameWindow, WHITE, (380, 50), 10, 0)
    pygame.draw.circle(gameWindow, BLACK, (380, 50), 10, 2)
    #arms
    pygame.draw.line(gameWindow,BLACK,(360,80),(380,70),2)
    pygame.draw.line(gameWindow,BLACK,(380,70),(400,70),2)
    #body
    pygame.draw.line(gameWindow,BLACK,(380,60),(380,80),2)
    #legs
    pygame.draw.line(gameWindow,BLACK,(380,80),(370,90),2)
    pygame.draw.line(gameWindow,BLACK,(380,80),(390,90),2)
    #stick/fishing rod
    if drawHand == False:
        pygame.draw.line(gameWindow,BLACK,(400,50),(400,90),3)
        
    if drawHat == True:
        gameWindow.blit(hats_display[hatNum],(370,30))
    if drawNeck == True:
        gameWindow.blit(necks_display[neckNum],(375,60))
    if drawShoe == True:
        gameWindow.blit(shoes_display[shoeNum],(362,90))
    if drawHand == True:
        gameWindow.blit(hands_display[handNum],(400,30))

#drawing the game window when the play is actually in play/catching fish
def redrawGameWindow():
    gameWindow.fill(LIGHTERBLUE)
    pygame.draw.line(gameWindow,BLACK,(LEFT,CENTERY),(WIDTH,CENTERY),1)
    drawVectorAndLine()
    drawLives()
    drawTimer()
    drawCounter()
    drawFish()
    drawCrab()
    drawSeahorse()
    drawLightningfish()
    drawShell()
    drawMenuButton()
    if canNextLevel:
        drawNextLevelButton()
    drawGameCharacter()
    pygame.display.update()

#drawing gameover screen/when user completes game or fails
def drawGameOverScreen():
    pygame.draw.rect(gameWindow, LIGHTBLUE, (100,100,600,400), 0)
    pygame.draw.rect(gameWindow, WHITE, (100,100,600,400), 5)
    menu = FONT_TITLE.render("GAME OVER",2,WHITE)
    gameWindow.blit(menu,(200,150))
    #space button to continue to closing page
    pygame.draw.rect(gameWindow, LIGHTERBLUE, (200,420,400,30), 0)
    pygame.draw.rect(gameWindow, WHITE, (200,420,400,30), 5)
    returnBack = FONT.render("Press SPACE to continue",2,WHITE)
    gameWindow.blit(returnBack,(270,420))
    pygame.display.update()

#drawing last closing page
def drawClosing():
    gameWindow.fill(LIGHTBLUE)
    over = FONT_TITLE.render("GAME OVER",2,WHITE)
    gameWindow.blit(over,(200,400))
    finalPoints = FONT_TITLE.render(str(points),2,WHITE)
    gameWindow.blit(finalPoints,(200,200))
    #restart button to start from beginning
    pygame.draw.rect(gameWindow, LIGHTBLUE, (650,30,100,50), 0)
    pygame.draw.rect(gameWindow, WHITE, (650,30,100,50), 5)
    restartButton = FONT.render("RESTART",2,WHITE)
    gameWindow.blit(restartButton,(655,40))
    if levelsComplete == True:
        complete = FONT.render("You have completed the game!",2,WHITE)
        gameWindow.blit(complete,(200,300))
    pygame.display.update()

#drawing next level screen when the user is about to proceed to the next level
def drawNextLevel():
    pygame.draw.rect(gameWindow, LIGHTBLUE, (100,100,600,400), 0)
    pygame.draw.rect(gameWindow, WHITE, (100,100,600,400), 5)
    nextLevel = FONT_TITLE.render("Next Level",2,WHITE)
    gameWindow.blit(nextLevel,(250,150))

    pygame.draw.rect(gameWindow, LIGHTERBLUE, (200,420,400,30), 0)
    pygame.draw.rect(gameWindow, WHITE, (200,420,400,30), 5)
    continueGame = FONT.render("Continue the game press SPACE",2,WHITE)
    gameWindow.blit(continueGame,(220,420))
    pygame.display.update()

#drawing complete game window when the user reaches level3 requirements
def completeGame():
    if levelsComplete ==True:
        pygame.draw.rect(gameWindow, LIGHTBLUE, (100,100,600,400), 0)
        pygame.draw.rect(gameWindow, WHITE, (100,100,600,400), 5)
        gameClear = FONT_TITLE.render("Completed",2,WHITE)
        gameWindow.blit(gameClear,(250,150))
        #space button
        pygame.draw.rect(gameWindow, LIGHTERBLUE, (200,420,400,30), 0)
        pygame.draw.rect(gameWindow, WHITE, (200,420,400,30), 5)
        continueToNext = FONT.render("Continue the game press SPACE",2,WHITE)
        gameWindow.blit(continueToNext,(220,420))
        pygame.display.update()

#to empty the lists before reassigning new values
def emptyLists():
    #fish
    for i in range (fishNum):
        fishX.pop()
        fishY.pop()
        fishR.pop()
        fishS.pop()
        fishDraw.pop()
    #seahorse
    for i in range (seaHorseNum):
        seaHorseX.pop()
        seaHorseY.pop()
        seaHorseR.pop()
        seaHorseS.pop()
        seaHorseDraw.pop()
    #crab
    for i in range (crabNum):
        crabX.pop()
        crabY.pop()
        crabR.pop()
        crabS.pop()
        crabDraw.pop()
    #lightning fish
    for i in range (lightNum):
        lightX.pop()
        lightY.pop()
        lightR.pop()
        lightS.pop()
        lightDraw.pop()
    #shells
    for i in range (shellNum):
        shellX.pop()
        shellY.pop()
        shellR.pop()
        shellP.pop()
        shellDraw.pop()

#assigning values to fish
def drawLists():
    for i in range (fishNum):
        fishX.append(randint(0, WIDTH/10)*10)
        fishY.append(randint(HEIGHT-580, HEIGHT/10)*10)
        fishR.append(fishRadius)
        fishS.append(randint(fishSpeedMin,fishSpeedMax))
        fishDraw.append(True)

    for i in range (seaHorseNum):
        seaHorseX.append(randint(0, WIDTH/10)*10)
        seaHorseY.append(randint(HEIGHT-580, HEIGHT/10)*10)
        seaHorseR.append(seaHorseRadius)
        seaHorseS.append(randint(seaHorseSpeedMin,seaHorseSpeedMax))
        seaHorseDraw.append(True)

    for i in range (crabNum):
        crabX.append(randint(0, WIDTH/10)*10)
        crabY.append(randint(HEIGHT-550, HEIGHT/10)*10)
        crabR.append(crabRadius)
        crabS.append(randint(crabSpeedMin,crabSpeedMax))
        crabDraw.append(True)

    for i in range (lightNum):
        lightX.append(randint(0, WIDTH/10)*10)
        lightY.append(randint(HEIGHT-550, HEIGHT/10)*10)
        lightR.append(lightRadius)
        lightS.append(randint(lightSpeedMin,lightSpeedMax))
        lightDraw.append(True)

    for i in range (shellNum):
        shellX.append(i*200+200)
        shellY.append(580)
        shellR.append(shellRadius)
        shellP.append(randint(shellLow,shellHigh))
        shellDraw.append(True)

#----------------------------------------#
#music
pygame.mixer.music.load('bgm2.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

#sound
Boing = pygame.mixer.Sound('Boing.wav')
Boing.set_volume(0.2)
Clip = pygame.mixer.Sound('Clip.wav')
Clip.set_volume(0.2)
Fizzle = pygame.mixer.Sound('Fizzle.wav')
Fizzle.set_volume(0.2)
#----------------------------------------#
notQuit = True
while notQuit:
    #opening page
    drawOpeningScreen()
    pygame.time.delay(5)
    openingMode = True
    while openingMode:
        for event in pygame.event.get():
            pygame.event.get()
            keys = pygame.key.get_pressed()
            (ballX,ballY)=pygame.mouse.get_pos()
            #pressing continue button
            if event.type == pygame.MOUSEBUTTONUP: 
                if ballX>=225 and ballX<=225+350 and ballY>= 550 and ballY<= 550+30:
                    openingMode = False
            #right key to continue, esc to quit entire game
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    openingMode = False
                elif event.key == pygame.K_ESCAPE:
                    openingMode = False
                    notQuit = False
                    pygame.quit()

    #----------------------------------------#
    #Rules page
    if notQuit == True:
        RuleMode = True
    else:
        RuleMode = False
        
    while RuleMode:
        drawRulesScreen()
        pygame.time.delay(5)
        for event in pygame.event.get():
            pygame.event.get()
            keys = pygame.key.get_pressed()
            (ballX,ballY)=pygame.mouse.get_pos()
            #pressing continue button
            if event.type == pygame.MOUSEBUTTONUP: ##release mouse
                if ballX>=225 and ballX<=225+350 and ballY>= 550 and ballY<= 550+30:
                    RuleMode = False
            #right key to continue, esc to quit entire game
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    RuleMode = False
                elif event.key == pygame.K_ESCAPE:
                    RuleMode = False
                    notQuit = False
                    pygame.quit()
        
    #----------------------------------------#
    #Avatar page
    if notQuit == True:
        avatarMode = True
    else:
        avatarMode = False

    #the index number of the selected item from its list
    selectedItem = 0
    
    #the index number of the hat
    hatNum = 0
    drawHat = False #True if the user picks a hat
    #neck item
    neckNum = 0
    drawNeck = False
    #shoes
    shoeNum = 0
    drawShoe = False
    #hand item
    handNum = 0
    drawHand = False
    
    while avatarMode:
        
        drawAvatarScreen()
        pygame.time.delay(5)

        for event in pygame.event.get():
            pygame.event.get()
            keys = pygame.key.get_pressed()
            (ballX,ballY)=pygame.mouse.get_pos()

            #the mouse clicks:
            if event.type == pygame.MOUSEBUTTONUP: ##release mouse
                #the continue button
                if ballX>=225 and ballX<=225+350 and ballY>= 550 and ballY<= 550+30:
                    avatarMode = False
                #the closet
                elif ballX>=350 and ballX<770:
                    #hats row
                    if ballY>=120 and ballY<=227:
                        selectedItem = (ballX-350)/140
                        hatNum = selectedItem
                        drawHat = True
                    #neck items row
                    elif ballY>=227 and ballY<=317:
                        selectedItem = (ballX-350)/140
                        neckNum = selectedItem
                        drawNeck = True
                    #shoes row
                    elif ballY>=317 and ballY<=407:
                        selectedItem = (ballX-350)/140
                        shoeNum = selectedItem
                        drawShoe = True
                    #hand held items row
                    elif ballY>=407 and ballY<=520:
                        selectedItem = (ballX-350)/140
                        handNum = selectedItem
                        drawHand = True

            #right to continue, esc to quit entire game
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    avatarMode = False
                elif event.key == pygame.K_ESCAPE:
                    avatarMode = False
                    notQuit = False
                    pygame.quit()

    #---------------------------------------#
    # properties                            #
    #---------------------------------------#

    #values for the fishing rod
    CENTERX = WIDTH/2
    CENTERY = HEIGHT-500
    VELOCITY = 10
    VECTOR = 50

    drawVector = True
    vectorX = 0
    vectorY = 0
    vectorAngle = 0
    rotationStep = 5
    direction = 1

    #the tip of the fishing rod
    drawLine = False
    objectX = WIDTH/2
    objectY = HEIGHT-500
    objectR = 10
    objectAngle = 0
    downUp = 1

#-------------------------------------------------
    #fish properties
    fishX = []
    fishY = []
    fishR = []
    fishS = []
    fishDraw = []

    fishHooked = -1 ##used to indicate which fish is caught from the list

    fishNum = 8
    fishRadius = 20
    fishSpeedMax = 3
    fishSpeedMin = 2
#---------------------------------------------------
    #seahorse properties
    seaHorseX = []
    seaHorseY = []
    seaHorseR = []
    seaHorseS = []
    seaHorseDraw = []

    seaHorseHooked = -1
    seaHorseNum = 3
    seaHorseRadius = 20
    seaHorseSpeedMax = 3
    seaHorseSpeedMin = 2
#----------------------------------------------------
    #crab properties
    crabX = []
    crabY = []
    crabR = []
    crabS = []
    crabDraw = []

    crabHooked = -1
    crabNum = 2
    crabRadius = 20
    crabSpeedMax = 3
    crabSpeedMin = 2
#-----------------------------------------------------
    #lightning fish properties
    lightX = []
    lightY = []
    lightR = []
    lightS = []
    lightDraw = []

    lightHooked = -1
    lightNum = 2
    lightRadius = 20
    lightSpeedMax = 3
    lightSpeedMin = 2

    shock = False
#---------------------------------------------------
    #shell properties
    shellX = []
    shellY = []
    shellR = []
    shellP = []
    shellDraw = []
    shellLow = 20
    shellHigh = 40
    shellHooked = -1
    shellNum = 3
    shellRadius = 45
#----------------------------------------------------
    changed = False#whether the direction of the rod (going down or up) is changed after contact with fish
    #append values inside the lists
    drawLists()
    
    #---------------------------------------#
    # main program                          #
    #---------------------------------------#
    #if the user can proceed to the next level without waiting for the time to pass
    canNextLevel = False
    clock = pygame.time.Clock()
    FPS = 30

    #basic setup values
    numberLives = 3
    points = 0
    timeLeft = 120
    timeBoost = 0

    #if the user has enough points to pass this level, turns to true and draws the next level button
    drawNext = False
    #draw the menu screen and pause the time if True
    drawingMenu = False
    #current level = level+1
    levels= 0
    #if the three levels are all completed
    levelsComplete = False

    if notQuit == True:
        inPlay = True
    else:
        inPlay = False

    #the three levels
    while levels>=0 and levels<3 and notQuit==True :
        #when going to the next level, display next level screen
        while drawNext:
            drawNextLevel()
            for event in pygame.event.get():
                pygame.event.get()
                keys = pygame.key.get_pressed()
                (ballX,ballY)=pygame.mouse.get_pos()
                #until mouse pressed continue button
                if event.type == pygame.MOUSEBUTTONUP:
                    if ballX>=200 and ballX<=200+400 and ballY>= 420 and ballY<= 420+30:
                        drawNext = False
                        inPlay= True
                #or space to continue
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        drawNext = False
                        inPlay= True
                    #escape to quit entire game
                    elif event.key == pygame.K_ESCAPE:
                        avatarMode = False
                        notQuit = False
                        pygame.quit()


        redrawGameWindow()
        #time entering the level
        BEGIN = pygame.time.get_ticks()
        timeLeft= 120
        #if enough points to proceed
        canNextLevel = False
        #if the user pressed next level button
        pressedNextLevel = False

        #time boosts from seahorse
        timeBoost = 0
        #time that the user presses the menu button to pause the game
        timePaused = 0
        #time that the user leaves the menu screen to continue playing
        timeUnpaused = 0
        
        while inPlay:
            #inplay of the current level
            redrawGameWindow()
            clock.tick(FPS)
            #wait for user to press key
            for event in pygame.event.get():
                pygame.event.get()
                keys = pygame.key.get_pressed()
                (ballX,ballY)=pygame.mouse.get_pos()
                
                if event.type == pygame.MOUSEBUTTONUP:
                    #menu button
                    if ballX>=650 and ballX<=650+100 and ballY>= 30 and ballY<= 30+50:
                        timePaused = (pygame.time.get_ticks())+timePaused
                        drawingMenu = True
                        #keep drawing menu
                        while drawingMenu:
                            drawMenu()
                            for event in pygame.event.get():
                                pygame.event.get()
                                (ballX,ballY)=pygame.mouse.get_pos()
                                if event.type == pygame.MOUSEBUTTONUP:
                                    #until user presses return back to game button
                                    if ballX>=200 and ballX<=200+400 and ballY>= 420 and ballY<= 420+30:
                                        timeUnpaused = (pygame.time.get_ticks())+timeUnpaused
                                        drawingMenu = False
                                #or quit entire game when quit key is pressed
                                elif event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_ESCAPE:
                                        inPlay = False
                                        notQuit = False
                                        pygame.quit()
                                        
                  #if the user presses the next level button
                    elif ballX>=500 and ballX<=500+100 and ballY>=30 and ballY<=30+50 and canNextLevel == True:
                       canNextLevel = False
                       pressedNextLevel = True
                       drawNext = True
                       inPlay = False
                elif event.type == pygame.KEYDOWN:
                #if the user presses space let down the hook
                    if drawLine == False and event.key == pygame.K_SPACE:
                        drawVector = False
                        drawLine = True
                        objectX = CENTERX
                        objectY = CENTERY
                        objectAngle = vectorAngle
                        downUp = 1
                        Boing.play()
                #if the user presses escape, quit the entire game
                    elif event.key == pygame.K_ESCAPE:
                        inPlay = False
                        notQuit = False
                        pygame.quit()

            #the time passed since entering this level
            #current time minus beginning time, and subtract the time spend on the menu when the game is paused
            elapsed = ((pygame.time.get_ticks() - BEGIN- timeUnpaused+timePaused)/1000)
            timeLeft = 120-elapsed+timeBoost
            
            #levels
            #8fish 3seahorse 2crab 2lightningfish 3seashells
            #level 1 requires 50 points to pass
            
            #6fish 2seahorse 2crab 2lightningfish 3seashells
            #level 2 requires 120 points to pass
            
            #4fish 2seahorse 3crab 3lightningfish
            #level 3 requires 200 points to complete game (or just continue to play until time up)

            #if the the time counts down to 0 or the user reaches point requirement and already pressed the next level button
            if timeLeft<=0 or pressedNextLevel:
                #moving from level 1 to 2
                if levels==0 and points>=50 and numberLives>0:
                    drawNext = True
                    levels = levels+1
                    timeBoost = 0
                    print "level 1 cleared"
                    emptyLists()
                    fishNum = 6
                    seaHorseNum = 2
                    shellNum = 3
                    shellHigh = shellHigh-5
                    drawLists()
                    inPlay = False
                #moving from level 2 to 3
                elif levels==1 and points>=120 and numberLives>0:
                    drawNext = True
                    levels = levels+1
                    timeBoost = 0
                    print "level 2 cleared"
                    emptyLists()
                    fishNum = 4
                    seaHorseNum = 2
                    crabNum = 3
                    lightNum = 3
                    shellNum = 3
                    shellHigh = shellHigh-5
                    drawLists()
                    inPlay = False
                #moving from level 3 to end
                elif levels==2 and points>=200 and numberLives>0:
                    print "level 3 cleared"
                    print "you have cleared the game"
                    levelsComplete = True
                    timeBoost = 0
                    levels = -1
                    inPlay = False
                #if not meet point requirement, go to game over
                else:
                    print "game over!"
                    levels = -1
                    inPlay = False
            #while theres still more time, if the user reaches the requirement, display the optional next level button
            elif timeLeft>0:
                if levels==0 and points>=50 and numberLives>0:
                    canNextLevel = True
                elif levels==1 and points>=120 and numberLives>0:
                    canNextLevel = True
                elif levels==2 and points>=200 and numberLives>0:
                    levelsComplete = True
            #game over of loses all three lives
            if numberLives==0:
                levels = -1
                inPlay = False

            #moving the fishing rod down
            objectX = objectX + downUp*int(round(VELOCITY*cos(objectAngle*pi/180)))
            objectY = objectY + downUp*int(round(VELOCITY*sin(objectAngle*pi/180)))

            if shock ==False:
                #make the fish swim
                for fish in range (len(fishX)):
                    fishX[fish] = fishX[fish]+fishS[fish]

                #make seahorse swim
                for seaHorse in range (len(seaHorseX)):
                    seaHorseX[seaHorse] = seaHorseX[seaHorse]+seaHorseS[seaHorse]

                #make crabs swim
                for crab in range (len(crabX)):
                    crabX[crab] = crabX[crab]+crabS[crab]

            #make light swim
            for light in range (len(lightX)):
                lightX[light] = lightX[light]+lightS[light]
                
            #keep swinging hook
            vectorAngle = (vectorAngle + (direction)*rotationStep)%180
            if vectorAngle == 0 or vectorAngle ==180:
                direction = -direction
                
            vectorX = int(round(VECTOR*cos(vectorAngle*pi/180)))
            vectorY = int(round(VECTOR*sin(vectorAngle*pi/180)))
            
        #################################################################################################################################
            #the following code requires too many parameters; can't be made into a function
            for fish in range (len(fishX)):
            #catching fish
                #make each of the if a function
                #if fishHooked< 0 and downUp>0 and distance(fishX[fish],fishY[fish],objectX,objectY)<fishR[fish] and drawLine==True:
                if fishHooked< 0 and downUp>0 and objectX >= fishX[fish]and objectX<=fishX[fish]+fishW and objectY>=fishY[fish] and objectY<=fishY[fish]+fishH and drawLine==True:
                    fishHooked = fish
                    if changed == False:
                        downUp = -downUp
                        changed = True

                if fishHooked >=0: #put the fish in the center of the hook
                    fishX[fishHooked] = objectX-fishW/2.0
                    fishY[fishHooked] = objectY
                    
                if fishY[fishHooked]<=CENTERY and fishDraw[fishHooked]==True: #after fish is caught, pop the caught fish and add a new one
                    points = points+1
                    changed = False
                    fishX[fishHooked]=randint(-WIDTH/100, 0)*10
                    fishY[fishHooked]=randint(HEIGHT-580, HEIGHT/10)*10
                    fishR[fishHooked]=fishRadius
                    fishS[fishHooked]=randint(fishSpeedMin,fishSpeedMax)
                    fishDraw[fishHooked]=True
                    fishHooked = -1

            for i in range(len(fishX)): # if fish swims past the right border, pop it and add new ones from the left
                if fishX[i]-fishR[i]>WIDTH:
                    fishX[i]=randint(-WIDTH/100, 0)*10
                    fishY[i]=randint(HEIGHT-580, HEIGHT/10)*10
                    fishR[i]=fishRadius
                    fishS[i]=randint(fishSpeedMin,fishSpeedMax)
                    fishDraw[i]=True
                    
        #################################################################################################################################
            for seaHorse in range (len(seaHorseX)):
            #catching seaHorse
                #if seaHorseHooked< 0 and downUp>0 and distance(seaHorseX[seaHorse],seaHorseY[seaHorse],objectX,objectY)<seaHorseR[seaHorse]and drawLine==True:
                if seaHorseHooked< 0 and downUp>0 and objectX >= seaHorseX[seaHorse]and objectX<=seaHorseX[seaHorse]+seahorseW and objectY>=seaHorseY[seaHorse] and objectY<=seaHorseY[seaHorse]+seahorseH and drawLine==True:
                    seaHorseHooked = seaHorse
                    if changed == False:
                        downUp = -downUp
                        changed = True

                if seaHorseHooked >=0: #put the fish in the center of the hook
                    seaHorseX[seaHorseHooked] = objectX-seahorseW/2.0
                    seaHorseY[seaHorseHooked] = objectY
                    
                if seaHorseY[seaHorseHooked]<=CENTERY and seaHorseDraw[seaHorseHooked]==True: #after fish is caught, pop the caught fish and add a new one
                    timeBoost = timeBoost+10
                    changed = False
                    seaHorseX[seaHorseHooked]=randint(-WIDTH/100, 0)*10
                    seaHorseY[seaHorseHooked]=randint(HEIGHT-580, HEIGHT/10)*10
                    seaHorseR[seaHorseHooked]=seaHorseRadius
                    seaHorseS[seaHorseHooked]=randint(seaHorseSpeedMin,seaHorseSpeedMax)
                    seaHorseDraw[seaHorseHooked]=True
                    seaHorseHooked = -1

            for i in range(len(seaHorseX)): # if fish swims past the right border, pop it and add new ones from the left
                if seaHorseX[i]-seaHorseR[i]>WIDTH:
                    seaHorseX[i]=randint(-WIDTH/100, 0)*10
                    seaHorseY[i]=randint(HEIGHT-580, HEIGHT/10)*10
                    seaHorseR[i]=seaHorseRadius
                    seaHorseS[i]=randint(seaHorseSpeedMin,seaHorseSpeedMax)
                    seaHorseDraw[i]=True
                    
        #################################################################################################################################
            for crab in range (len(crabX)):
            #catching crab
                #if crabHooked< 0 and downUp>0 and distance(crabX[crab],crabY[crab],objectX,objectY)<crabR[crab]and drawLine==True:
                if crabHooked< 0 and downUp>0 and objectX >= crabX[crab]and objectX<=crabX[crab]+crabW and objectY>=crabY[crab] and objectY<=crabY[crab]+crabH and drawLine==True:
                    crabHooked = crab
                    Clip.play()
                    if changed == False:
                        downUp = -downUp
                        changed = True

                if crabHooked >=0: #put the fish in the center of the hook
                    crabX[crabHooked] = objectX-crabW/2.0
                    crabY[crabHooked] = objectY
                    
                if crabY[crabHooked]<=CENTERY and crabDraw[crabHooked]==True: #after fish is caught, pop the caught fish and add a new one
                    changed = False
                    crabX[crabHooked]=randint(-WIDTH/100, 0)*10
                    crabY[crabHooked]=randint(HEIGHT-580, HEIGHT/10)*10
                    crabR[crabHooked]=crabRadius
                    crabS[crabHooked]=randint(crabSpeedMin,crabSpeedMax)
                    crabDraw[crabHooked]=True
                    crabHooked = -1
                    numberLives = numberLives-1
                    points = points+5

            for i in range(len(crabX)): # if fish swims past the right border, pop it and add new ones from the left
                if crabX[i]-crabR[i]>WIDTH:
                    crabX[i]=randint(-WIDTH/100, 0)*10
                    crabY[i]=randint(HEIGHT-580, HEIGHT/10)*10
                    crabR[i]=crabRadius
                    crabS[i]=randint(crabSpeedMin,crabSpeedMax)
                    crabDraw[i]=True
                    
        #################################################################################################################################
            for light in range (len(lightX)):
            #catching light
                if lightHooked< 0 and downUp>0 and distance(lightX[light],lightY[light],objectX,objectY)<lightR[light]and drawLine==True:
                    lightHooked = light
                    shock = True
                    Fizzle.play()
                    if changed == False:
                        downUp = -downUp
                        changed = True

                if lightHooked >=0: #put the fish in the center of the hook
                    lightX[lightHooked] = objectX
                    lightY[lightHooked] = objectY
                    
                if lightY[lightHooked]<=CENTERY and lightDraw[lightHooked]==True: #after fish is caught, pop the caught fish and add a new one
                    changed = False
                    shock = False
                    lightX[lightHooked]=randint(-WIDTH/100, 0)*10
                    lightY[lightHooked]=randint(HEIGHT-580, HEIGHT/10)*10
                    lightR[lightHooked]=lightRadius
                    lightS[lightHooked]=randint(lightSpeedMin,lightSpeedMax)
                    lightDraw[lightHooked]=True
                    lightHooked = -1
                    numberLives = numberLives-1
                    points = points+10


            for i in range(len(lightX)): # if fish swims past the right border, pop it and add new ones from the left
                if lightX[i]-lightR[i]>WIDTH:
                    lightX[i]=randint(-WIDTH/100, 0)*10
                    lightY[i]=randint(HEIGHT-580, HEIGHT/10)*10
                    lightR[i]=lightRadius
                    lightS[i]=randint(lightSpeedMin,lightSpeedMax)
                    lightDraw[i]=True
                    
        #################################################################################################################################
            for shell in range (len(shellX)):
            #catching shell
                if shellHooked< 0 and downUp>0 and distance(shellX[shell],shellY[shell],objectX,objectY)<shellR[shell]and drawLine==True:
                    shellHooked = shell
                    if changed == False:
                        downUp = -downUp
                        changed = True

            if shellHooked >=0: #put the fish in the center of the hook
                shellX[shellHooked] = objectX
                shellY[shellHooked] = objectY
                
            if shellY[shellHooked]<=CENTERY and shellDraw[shellHooked]==True: #after fish is caught, pop the caught fish
                changed = False
                shellX[shellHooked]=0
                shellY[shellHooked]=0
                shellR[shellHooked]=0
                shellDraw[shellHooked]=False
                shellHooked = -1
                points = points+shellP[shell]
                
        ################################################################################################################################
            #pull hook up if touches border
            if objectX>WIDTH or objectX<0 or objectY>HEIGHT or objectY<0:
                downUp = -downUp
           
            #when the hook returns back, change back to swinging mode
            if objectX == CENTERX and objectY == CENTERY:
                downUp = 0
                drawLine = False
                drawVector = True
        ####################################################################################################################################

    #---------------------------------------#
    #closing screen
    if notQuit == True:
        closingMode = False
    else:
        closingMode = True
        
    while levels<0 and closingMode == False:
        if levelsComplete==True:
            completeGame()
        else:
            drawGameOverScreen()
        for event in pygame.event.get():
            pygame.event.get()
            keys = pygame.key.get_pressed()
            (ballX,ballY)=pygame.mouse.get_pos()
            #press the button to continue to final page
            if event.type == pygame.MOUSEBUTTONUP:
                if ballX>=200 and ballX<=200+400 and ballY>= 420 and ballY<= 420+30:
                    closingMode = True
            #space to continue, esc to quit entire game
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    closingMode = True
                elif event.key == pygame.K_ESCAPE:
                    closingMode = True
                    notQuit = False
                    pygame.quit()
    #---------------------------------------#
    if notQuit == True:
        closingMode = True
    else:
        closingMode = False
        
    while closingMode == True:
        drawClosing()
        for event in pygame.event.get():
            pygame.event.get()
            keys = pygame.key.get_pressed()
            (ballX,ballY)=pygame.mouse.get_pos()
            #restart button
            if event.type == pygame.MOUSEBUTTONUP:
                if ballX>=650 and ballX<=650+100 and ballY>= 30 and ballY<= 30+50:
                    print "restart game"
                    closingMode = False
            #esc to quit entire game
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    closingMode = False
                    notQuit = False
                    pygame.quit()
