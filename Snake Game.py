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
pygame.display.set_caption("Images/I Am Groot")
icon = pygame.image.load("Images/Groot Icon.png")
pygame.display.set_icon(icon)
gameLogo = pygame.image.load("Images/Groot Logo.png")
# mrbean = pygame.image.load("Mr Bean.png")
background = pygame.image.load("Images/Background.png")

# player coordinates (size = 49x64)
# playerImg = pygame.image.load("I Am Groot.png")
# playerBody = pygame.image.load("I Am Groot.png")

# player coordinates (size = 25x25)
playerImg = pygame.image.load("Images/Groot Face.png")
playerBody = pygame.image.load("Images/Groot Face.png")

# frame coordinates (size = 400x400)
frameImg = pygame.image.load("Images/frame.png")


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
for j in range(50,425,25):
    for i in range(125,500,25):
        foodCoordinates.append((i,j))

def randomFoodPos(x,y):
    z=[]
    for i in x:
        if i not in y:
            z.append(i)
            (foodX,foodY) = random.choice(z)
    return (foodX,foodY)

(foodX,foodY) = randomFoodPos(foodCoordinates,[])

class body:
    def __init__(self,x):
        self.x = x

    def my_func(self):
        screen.blit(playerBody,self.x)

# score function
def scoreValue(text,x,y):
    currentScore = score_font.render(text, True, (255,255,255))
    screen.blit(currentScore, (x,y))
    
# player, food, frame function
def player(x,y):
    screen.blit(playerImg, (x,y))

def newFood(x,y):
    screen.blit(food,(x,y))

def frame():
    screen.blit(frameImg,(115,40))

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
            
            # if key is pressed, check whether it's right or left
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
    playerX = 275
    playerY = 350
    playerX_change = 0
    playerY_change = 0
    score = 0
    speed=0.5
    scoreX = 500
    scoreY = 20
    movingCoordinates = []
    currentBody = []
    arrayValues = [-2]
    (foodX,foodY) = randomFoodPos(foodCoordinates,[])
    # print((foodX,foodY))

    with open ("highscore.txt","r") as f:
        highscore = f.read()

    while not game_exit:
        if game_over:

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
            # RGB - Red, Green
            # screen.fill((0,0,0))
            screen.blit(background,(0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    game_exit = True
                
                # if key is pressed, check whether it's right or left
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and not playerX_change == 25:
                        playerX_change = -25
                        playerY_change = 0
                    if event.key == pygame.K_RIGHT and not playerX_change == -25:
                        playerX_change = 25
                        playerY_change = 0
                    if event.key == pygame.K_UP and not playerY_change == 25:
                        playerY_change = -25
                        playerX_change = 0
                    if event.key == pygame.K_DOWN and not playerY_change == -25:
                        playerY_change = 25
                        playerX_change = 0

            playerX += playerX_change
            playerY += playerY_change

            if playerX_change == 0 and playerY_change == 0:
                print("Press Any Arrow Key To Start")
            
            else:
                movingCoordinates.append((playerX,playerY))
                currentBody = [(playerX,playerY)]
                print("PlayerX, PlayerY = ",(playerX,playerY))
                # print("FoodX, FoodY     = ",(foodX,foodY))
                if len(movingCoordinates) >= 2: 
                    for i in arrayValues:
                        py = body(movingCoordinates[i])
                        py.my_func()
                        currentBody.append(movingCoordinates[i])
                        if (playerX,playerY) == movingCoordinates[i]:
                            game_over = True

            newFood(foodX,foodY)
            player(playerX,playerY)
            frame()

            if playerX == 100 or playerX == 500 or playerY == 25 or playerY == 425:
                playerY_change = 0
                playerX_change = 0
                game_over = True
                    
            if foodX == playerX and foodY == playerY:
                AppleCrunch = mixer.Sound('Audios/Apple Crunch.wav')
                AppleCrunch.play()
                score += 100
                arrayValues.append((arrayValues[-1])-1)
                print("\n            Eaten\n        New Speed : ", round(speed,2), "\n")
                if score % 300 == 0:
                    speed=speed*0.80
                foodX, foodY = randomFoodPos(foodCoordinates,currentBody)
                if score > int(highscore):
                    highscore = score
            scoreValue("Score = " + str(score), scoreX,scoreY)
            
        pygame.display.update()
        time.sleep(speed)
        clock.tick(60)

    pygame.quit()
    quit()

GameIntro()




