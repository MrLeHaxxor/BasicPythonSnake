import pygame
import random

#global system values
win = None
font = None
keys = None
direction = [10,0]
snake = None
delta = 0
speed = 140
updateTimer = 0
gametime = 0
score = 0
hiScore = 0
fruitX = 0
fruitY = 0

secondtimer = 0
fps = 0
fpscounter = 0
#please
def trackFPS():
    global secondtimer, fpscounter,fps
    if delta > 0:
        fps = 1000 / delta
    #secondtimer += delta
    #fpscounter += 1
    #if secondtimer > 1000:
    #    secondtimer -= 1000
    #    fps = fpscounter
    #    fpscounter = 0


def gameLoop():
    global keys, delta, gametime, secondtimer, fpscounter
    running = True
    while running:
        delta = pygame.time.get_ticks() - gametime
        gametime += delta
        
        #trackFPS()

        keys = pygame.key.get_pressed()
        gameLogic()

        if keys[pygame.K_ESCAPE]:
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

def InitialiseGame():
    global status,updateTimer,gametime, speed, score, snake, direction
    win.fill((0,0,0))
    win.blit(font.render("GET READY", False, (90,90,255)), (150,200))
    pygame.display.flip()
    pygame.time.delay(2000)
    score = 0
    updateTimer=0
    speed = 80
    snake = [[220,190],[210,190],[200,190],[190,190],[180,190],[170,190]]
    direction = [10,0]
    newFruit()
    gametime = pygame.time.get_ticks()

def newFruit():
    global fruitX,fruitY
    while True:
        fruitX = random.randint(2,36) * 10
        fruitY = random.randint(2,36) * 10
        pos = [fruitX, fruitY]
        if (not pos in snake):
            break

def gameLogic():
    global updateTimer, score, speed
           
    gameKeys()
    updateTimer += delta
    if (updateTimer > speed):
        updateTimer -= speed
        headX = snake[0][0] + direction[0]
        headY = snake[0][1] + direction[1]
        snake.insert(0, [headX, headY])
        #collisions
        if (snake[0][0] < 0 or snake[0][0] > 390 or 
            snake[0][1] < 0 or snake[0][1] > 390):
                endGame()
        elif snake[0] in snake[1:]: #hit yourself
            endGame()
        elif (fruitX == snake[0][0] and fruitY == snake[0][1]):
            score += 1
            speed -= 1
            newFruit()
        else:
            snake.pop()

    drawGame()

def gameKeys():
    global direction
    if keys[pygame.K_LEFT]:
        direction = [-10,0]
    if keys[pygame.K_RIGHT]:
        direction = [10,0]
    if keys[pygame.K_UP]:
        direction = [0,-10]
    if keys[pygame.K_DOWN]:
        direction = [0,10]

def drawGame():
    win.fill((0,0,0))
    for piece in snake[1:]:
        pygame.draw.rect(win, (255,0,0), (piece[0], piece[1], 10, 10))
    pygame.draw.rect(win, (255,200,200), (snake[0][0], snake[0][1], 10, 10))

    pygame.draw.rect(win, (0,255,0), (fruitX, fruitY, 10, 10))

    win.blit(font.render("score " +str(score), False, (255,255,255)), (10,10))
    win.blit(font.render("h-score " +str(hiScore), False, (255,255,0)), (280,10))
    win.blit(font.render("fps " +str(fps), False, (255,255,255)), (190,0))

    pygame.display.flip()

def endGame():
    global hiScore
    if (score > hiScore):
        hiScore = score
    win.blit(font.render("Doh!", False, (255,200,200)), (150,200))
    pygame.display.flip()

    pygame.time.delay(2000)
    InitialiseGame()

#=== start point of code ===#    
pygame.init()
win = pygame.display.set_mode((400, 400))
font = pygame.font.SysFont("monospace",20)
InitialiseGame()
gameLoop()
pygame.quit()
