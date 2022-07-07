import pygame
import time
import random
from pygame import mixer


# Initialize
pygame.init()

clock = pygame.time.Clock()

# creating screen - coordinates (width , height)
screen = pygame.display.set_mode((600,450))

# Title & Icon & Logo
pygame.display.set_caption("I Am Groot")
icon = pygame.image.load("Images/Groot Icon.png")
pygame.display.set_icon(icon)
background = pygame.image.load("Images/Background.png")
gameLogo = pygame.image.load("Images/Groot Logo.png")
background = pygame.image.load("Images/Background.png")

# player coordinates (size = 25x25)
playerImg = pygame.image.load("Images/Groot Face 1.png")
playerBody = pygame.image.load("Images/Groot Face 2.png")
playerTail = pygame.image.load("Images/Groot Face.png")

# frame coordinates (size = 400x400)
frameImg = pygame.image.load("Images/Frame1.png")
frameX=155
frameY=80


# score
score = 0

# fonts
welcome_font = pygame.font.Font('Fonts/alger.ttf', 40)
gameStart_font = pygame.font.Font('Fonts/georgiaz.ttf', 24)
score_font = pygame.font.Font('freesansbold.ttf', 16)
game_over_font = pygame.font.Font('Fonts/seasrn.ttf', 64)
game_over_score = pygame.font.Font('Fonts/alger.ttf', 40)
high_score = pygame.font.Font('Fonts/alger.ttf', 32)
thankYou_font = pygame.font.Font('freesansbold.ttf', 20)
playAgain_font = pygame.font.Font('Fonts/georgiaz.ttf', 16)

# food coordinates (size = 25x25)
food = pygame.image.load("Images/food.png")

foodCoordinates = []
for j in range(100,350,25):
    for i in range(175,425,25):
        foodCoordinates.append((i,j))

def randomFoodPos(x,y):
    z=[]
    for i in x:
        if i not in y:
            z.append(i)
            (foodX,foodY) = random.choice(z)
    if len(z)==0:
        eternity()
    return (foodX,foodY)

(foodX,foodY) = randomFoodPos(foodCoordinates,[])

class body:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def my_func(self):
        screen.blit(playerBody,self.x)
        screen.blit(playerTail,self.y)


# score function
def scoreValue(text):
    currentScore = score_font.render(text, True, (255,255,255))
    screen.blit(currentScore, (450,20))
    
# player, food, frame function
def player(x,y):
    screen.blit(playerImg, (x,y))

def newFood(x,y):
    screen.blit(food,(x,y))

def frame():
    screen.blit(frameImg,(frameX,frameY))

# *******************************************************************************************************************************************

def hamiltonianCycle(x,y):

    z=[]

    if x==175 and y!=325:
        playerX_change = 0
        playerY_change = 25

    if (x!=400 and y==325) or (x!=400 and x!=175 and y%50==25):
        playerX_change = 25
        playerY_change = 0

    if (x==400 and y%50==25) or (x==200 and y%50==0 and y!=100):
        playerX_change = 0
        playerY_change = -25

    if (x!=175 and x!=200 and y%50==0) or (x==200 and y==100):
        playerX_change = -25
        playerY_change = 0

    return playerX_change, playerY_change

# *******************************************************************************************************************************************

def directCatch(playerX,playerY,foodX,foodY):
    if playerX > foodX:
        playerX_change = -25
        playerY_change = 0

    if playerX < foodX:
        playerX_change = 25
        playerY_change = 0

    if (playerX == foodX) and playerY > foodY:
        playerY_change = -25
        playerX_change = 0

    if (playerX == foodX) and playerY < foodY:
        playerY_change = 25
        playerX_change = 0

    return playerX_change, playerY_change

# *******************************************************************************************************************************************

def GameIntro():
    game_exit=False

    while not game_exit:
        # screen.fill((0,0,255))
        screen.blit(background,(0,0))
        screen.blit(gameLogo,(80,120))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                    game_exit = True

        time.sleep(1.5)
        GameIntro = mixer.Sound('Audios/I Am Groot.wav')
        GameIntro.play()
        time.sleep(1.5)
        welcome()

        pygame.quit()
        quit()

def eternity():

    time.sleep(3)
    
    WelcomeX = mixer.Sound('Audios/WelcomeX.wav')
    WelcomeX.play()
    game_exit=False

    while not game_exit:
        # screen.fill((0,0,0))
        screen.blit(background,(0,0))
        welcomeText = welcome_font.render("You Reached Eternity !", True, (238,75,43))
        gameStart = gameStart_font.render("Press SPACEBAR To Play Again & 1 To Quit", True, (238,75,43))

        screen.blit(welcomeText, (60,175))
        screen.blit(gameStart, (35,250))

        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                game_exit = True
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

                if event.key == pygame.K_1:
                        game_exit = True

        pygame.display.update()
        time.sleep(0.5)

def welcome():
    
    WelcomeX = mixer.Sound('Audios/WelcomeX.wav')
    WelcomeX.play()
    game_exit=False

    while not game_exit:
        # screen.fill((0,0,0))
        screen.blit(background,(0,0))
        welcomeText = welcome_font.render("Welcome To Groot Run !", True, (238,75,43))
        gameStart = gameStart_font.render("Press SPACEBAR To Play", True, (238,75,43))
        screen.blit(welcomeText, (60,175))
        screen.blit(gameStart, (150,250))

        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                game_exit = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
                   
        pygame.display.update()
        time.sleep(0.5)

# game (main)
def game():
    
    mixer.music.load('Audios/Background Music.wav')
    mixer.music.play(-1)

    game_exit = False
    game_over = False
    playerX = 200
    playerY = 275
    playerX_change = 0
    playerY_change = 0
    score = 0
    speed= 0.05
    movingCoordinates = []
    currentBody = [(playerX,playerY)]
    arrayValues = [-2]
    (foodX,foodY) = randomFoodPos(foodCoordinates,[])

    with open ("highscore.txt","r") as f:
        highscore = f.read()

    while not game_exit:
        if game_over:

            time.sleep(3)

            with open ("highscore.txt","w") as f:
                f.write(str(highscore))

            # screen.fill((0,0,0))
            screen.blit(background,(0,0))

            gameOverText = game_over_font.render("GAME OVER !", True, (238,75,43))
            totalScore = game_over_score.render("Score : " + str(score), True, (238,75,43))
            highScore = high_score.render("High Score : "  + str(highscore), True, (238,75,43))
            thankYouText = thankYou_font.render("Thank You For Playing", True, (238,75,43))
            playAgainText = playAgain_font.render("Press 1 To Play Again & 2 To Quit", True, (238,75,43))

            screen.blit(gameOverText, (75,150))
            screen.blit(totalScore, (200,230))
            screen.blit(highScore, (160,275))
            screen.blit(thankYouText, (175,350))
            screen.blit(playAgainText, (150,375))

            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        print("\n             Game Over \n            Score = " + str(score))
                        welcome()
                    if event.key == pygame.K_2:
                        game_exit = True

        else:
            screen.blit(background,(0,0))

            if len(currentBody) >= 1:
                currentplayerX_change = playerX_change

                if playerX!=175 and ((playerX<=foodX and playerY>foodY) and (foodY>currentBody[-1][-1] or playerY<=currentBody[-1][-1] or (foodX!=175 and currentBody[-1][0]==175))):
                    playerX_change,playerY_change = directCatch(playerX,playerY,foodX,foodY)
                    
                    if currentplayerX_change == - playerX_change and playerX_change!=0:
                        playerX_change,playerY_change = hamiltonianCycle(playerX,playerY)

                if (currentBody[-1][0]!=175 and currentBody[-1][-1]>foodY and playerY>=currentBody[-1][-1]) or playerX==175 or (playerX>foodX and playerY>foodY) or playerY<=foodY or foodY==currentBody[-1][-1]:
                    playerX_change,playerY_change = hamiltonianCycle(playerX,playerY)

                if playerX!=175 and playerX!=400 and playerX_change!=25 and playerY<foodY and playerY<currentBody[-1][-1]:
                    playerX_change = -25
                    playerY_change = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    game_exit = True

            playerX += playerX_change
            playerY += playerY_change

            if playerX_change == 0 and playerY_change == 0:
                print("Press Any Arrow Key To Start")
            
            else:
                movingCoordinates.append((playerX,playerY))
                currentBody = [(playerX,playerY)]
                if len(movingCoordinates) >= 2:
                    for i in arrayValues:
                        py = body(movingCoordinates[i], currentBody[-1])
                        py.my_func()
                        currentBody.append(movingCoordinates[i])

            newFood(foodX,foodY)
            player(playerX,playerY)
            frame()

            if playerX == 150 or playerX == 425 or playerY == 75 or playerY == 350:
                playerY_change = 0
                playerX_change = 0
                game_over = True
                    
            if foodX == playerX and foodY == playerY:
                AppleCrunch = mixer.Sound('Audios/Apple Crunch.wav')
                AppleCrunch.play()
                score += 100
                arrayValues.append((arrayValues[-1])-1)
                print("\n            Eaten\n        New Speed : ", round(speed,5), "\n")
                if score % 300 == 0:
                    speed=speed*0.80
                foodX, foodY = randomFoodPos(foodCoordinates,currentBody)
                # print(currentBody)
                if score > int(highscore):
                    highscore = score
            scoreValue("Score = " + str(score))
        
        pygame.display.update()
        time.sleep(speed)
        clock.tick(60)

    pygame.quit()
    quit()

GameIntro()




