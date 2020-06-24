import pygame
import time
import random


# Initialize pygame in order to actually make the game
pygame.init()

screen = pygame.display.set_mode((625, 625))

# Game Setup
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

def main():
    wallCount = 0
    wallXArr = []
    wallYArr = []
    pre_game = True
    running = True
    while pre_game:
        titleFont = pygame.font.Font("freesansbold.ttf", 32)
        title = titleFont.render("SNAKE", True, (255, 255, 255), (0, 0, 0))
        titleRect = title.get_rect()
        titleRect.center = (625 / 2, 625 / 8)
        screen.blit(title, titleRect)

        font = pygame.font.Font("freesansbold.ttf", 20)
        movementInstructions = font.render("USE ARROW KEYS TO COLLECT APPLES", True, (255, 255, 255), (0, 0, 0))
        movementRect = movementInstructions.get_rect()
        movementRect.center = (625 / 2, (625 / 8) * 2)
        screen.blit(movementInstructions, movementRect)

        font = pygame.font.Font("freesansbold.ttf", 20)
        collisionInstructions = font.render("DON'T COLLIDE INTO YOURSELF OR WALLS", True, (255, 255, 255), (0, 0, 0))
        collisionRect = collisionInstructions.get_rect()
        collisionRect.center = (625 / 2, (625 / 8) * 3)
        screen.blit(collisionInstructions, collisionRect)

        font = pygame.font.Font("freesansbold.ttf", 20)
        gridInstructions = font.render("""PRESS "G" TO TOGGLE GRID""", True, (255, 255, 255), (0, 0, 0))
        gridRect = gridInstructions.get_rect()
        gridRect.center = (625 / 2, (625 / 8) * 4)
        screen.blit(gridInstructions, gridRect)

        font = pygame.font.Font("freesansbold.ttf", 20)
        playInstructions = font.render("""PRESS SPACE TO GO TO THE GAME""", True, (255, 255, 255), (0, 0, 0))
        playRect = playInstructions.get_rect()
        playRect.center = (625 / 2, (625 / 8) * 5)
        screen.blit(playInstructions, playRect)

        font = pygame.font.Font("freesansbold.ttf", 20)
        restartInstructions = font.render("""PRESS "R" AT ANY TIME TO RESTART""", True, (255, 255, 255), (0, 0, 0))
        restartRect = restartInstructions.get_rect()
        restartRect.center = (625 / 2, (625 / 8) * 6)
        screen.blit(restartInstructions, restartRect)



        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pre_game = False

            if event.type == pygame.QUIT:
                pre_game = False
                running = False


            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    pre_game = False
                    running = False



    # Setting up the player
    snakeImg = []
    snakeImg.append(pygame.image.load('snakeBody.PNG'))
    snakeImg[0] = pygame.transform.scale(snakeImg[0], (25, 25))
    snakeX = []
    snakeY = []
    snakeX.append(200)
    snakeY.append(200)
    snake_X_Change = 0
    snake_Y_Change = 0


    # Setting up the apple
    appleImg = pygame.image.load('snakeApple.PNG')
    appleImg = pygame.transform.scale(appleImg, (25, 25))
    appleX = 300
    appleY = 300
    apple_X_Change = 0
    apple_Y_Change = 0

    # Game Over Set Up (Must be done before all game code)
    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render("Game Over!", True, (0, 255, 0), (0, 0, 255))
    wordRect = text.get_rect()
    wordRect.center = (625 / 2, 625 / 8)

    value = 0
    def score(x,y):
        score = font.render("Score: " + str(value), True, (255, 255, 255))
        screen.blit(score, (x,y))

    def player(x, y, index):
        screen.blit(snakeImg[index], (x, y))


    def apple(x, y):
        screen.blit(appleImg, (x, y))


    def grid(toggle):
        if toggle:
            numRows = 25
            x = 0
            y = 0
            for i in range(25):
                pygame.draw.line(screen, (73, 3, 252), (x, 0), (x, 625))
                x += 25
            for i in range(25):
                pygame.draw.line(screen, (73, 3, 252), (0, y), (625, y))
                y += 25
        else:
            screen.fill((0, 0, 0))

    def wallDraw(clickedX, clickedY):
        xPos = clickedX - (clickedX % 25)
        yPos = clickedY - (clickedY % 25)
        pygame.draw.rect(screen,(192,192,192),(xPos,yPos,25,25))





    # This is the loop for the game below that runs until we quit
    game_over = False
    notGrid = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return main()
                if event.key == pygame.K_LEFT:
                    snake_Y_Change = 0
                    snake_X_Change = -25
                if event.key == pygame.K_RIGHT:
                    snake_Y_Change = 0
                    snake_X_Change = 25
                if event.key == pygame.K_UP:
                    snake_X_Change = 0
                    snake_Y_Change = -25
                if event.key == pygame.K_DOWN:
                    snake_X_Change = 0
                    snake_Y_Change = 25
                if event.key == pygame.K_g:
                    if notGrid:
                        notGrid = False
                    else:
                        notGrid = True

        if notGrid:
            grid(False)
        else:
            grid(True)


        oldX = snakeX[:]
        oldY = snakeY[:]

        if value > 0:
            if snakeX[0] + snake_X_Change == snakeX[1] and snakeY[0] + snake_Y_Change == snakeY[1]:
                snake_X_Change = oldXChange
                snake_Y_Change = oldYChange


        snakeX[0] += snake_X_Change
        snakeY[0] += snake_Y_Change

        for i in range(len(snakeX)):
            if i != 0:
                snakeX[i] = oldX[i-1]
                snakeY[i] = oldY[i-1]

#Drawing of the walls ------------------------------------------------------

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                currentPos = pygame.mouse.get_pos()
                wallXArr.append(currentPos[0])
                wallYArr.append(currentPos[1])
                pygame.draw.rect(screen, (192, 192, 192),(currentPos[0] - (currentPos[0] % 25), currentPos[1] - (currentPos[1] % 25), 25, 25))


        for i in range(len(wallXArr)):
            if snakeX[0] == wallXArr[i] and snakeY[0] == wallYArr[i]:
                game_over = True
            pygame.draw.rect(screen, (192, 192, 192), (wallXArr[i] - (wallXArr[i] % 25), wallYArr[i] - (wallYArr[i] % 25), 25, 25))




#---------------------------------------------------------------------------

        if snakeX[0] < 0:
            game_over = True
        elif snakeX[0] >= 625:
            game_over = True
        elif snakeY[0] < 0:
            game_over = True
        elif snakeY[0] >= 625:
            game_over = True
        for i in range(len(wallXArr)):
            if snakeX[0] == wallXArr[i] - (wallXArr[i] % 25) and snakeY[0] == wallYArr[i] - (wallYArr[i] % 25):
                game_over = True




        if appleX == snakeX[0] and appleY == snakeY[0]:
            wallXArr = []
            wallYArr = []
            value += 1
            appleX = random.randint(0,24) * 25
            appleY = random.randint(0,24) * 25

            for i in range(len(snakeX)):
                while appleX == snakeX[i] and appleY == snakeY[i]:
                    appleX = random.randint(0, 24) * 25
                    appleY = random.randint(0, 24) * 25

            snakeImg.append(pygame.image.load('snakeBody.PNG'))
            snakeImg[value] = pygame.transform.scale(snakeImg[value], (25, 25))
            snakeX.append(oldX[value - 1])
            snakeY.append(oldY[value - 1])
            print(snakeX[value])

        for i in range(len(snakeX)):
            for j in range(len(snakeY)):
                 if i != j:
                    if snakeX[i] == snakeX[j] and snakeY[i] == snakeY[j]:
                            game_over = True


        apple(appleX, appleY)

        if game_over == True:
            screen.fill((0, 0, 0))
            snake_X_Change = 0
            snake_Y_Change = 0
            screen.blit(text, wordRect)

        for i in range(len(snakeX)):
            player(snakeX[i], snakeY[i], i)

        oldXChange = snake_X_Change
        oldYChange = snake_Y_Change

        score(10, 10)
        if game_over == True:
            screen.fill((0, 0, 0))
            snake_X_Change = 0
            snake_Y_Change = 0
            screen.blit(text, wordRect)
            font = pygame.font.Font("freesansbold.ttf", 20)
            restartInstructions = font.render("""PRESS "R" TO RESTART""", True, (255, 255, 255), (0, 0, 0))
            restartRect = restartInstructions.get_rect()
            restartRect.center = (625 / 2, (625 / 8) * 3)
            screen.blit(restartInstructions, restartRect)
                #font = pygame.font.Font("freesansbold.ttf", 20)
                #restartInstructions = font.render("""PRESS R TO RESTART AND PLAY AGAIN""", True, (255, 255, 255), (0, 0, 0))
                #playRect = playInstructions.get_rect()
                #playRect.center = (625 / 2, (625 / 8) * 5)
                #screen.blit(playInstructions, playRect)
        pygame.display.update()

        time.sleep(0.09)


main()

