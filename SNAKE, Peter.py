
import pygame,sys,time,random
from pygame.locals import *
#  make color
red = pygame.Color(255,0,0)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
grey = pygame.Color(150,150,150)

# gameover
def gameOver(playSurface):
    gameOverFont = pygame.font.Font('arial.ttf',72)
    gameOverSurf = gameOverFont.render('Game Over', True, grey)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 10)
    playSurface.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

# main
def main():
    # initialized
    pygame.init()
    fps = pygame.time.Clock()
    playSurface = pygame.display.set_mode((640,480))
    pygame.display.set_caption('apple Snake')

    # initialized variable
    snakePosition = [100,100]
    snakeSegments = [[100,100],[80,100],[60,100]]
    applePosition = [300,300]
    appleleft = 1
    direction = 'right'
    changeDirection = direction
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:

                if event.key == K_RIGHT or event.key == ord('d'):
                    changeDirection = 'right'
                if event.key == K_LEFT or event.key == ord('a'):
                    changeDirection = 'left'
                if event.key == K_UP or event.key == ord('w'):
                    changeDirection = 'up'
                if event.key == K_DOWN or event.key == ord('s'):
                    changeDirection = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

        if changeDirection == 'right' and not direction == 'left':
            direction = changeDirection
        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection
        if changeDirection == 'up' and not direction == 'down':
            direction = changeDirection
        if changeDirection == 'down' and not direction == 'up':
            direction = changeDirection

        if direction == 'right':
            snakePosition[0] += 20
        if direction == 'left':
            snakePosition[0] -= 20
        if direction == 'up':
            snakePosition[1] -= 20
        if direction == 'down':
            snakePosition[1] += 20

        snakeSegments.insert(0,list(snakePosition))

        if snakePosition[0] == applePosition[0] and snakePosition[1] == applePosition[1]:
            appleleft = 0
        else:
            snakeSegments.pop()

        if appleleft == 0:
            x = random.randrange(1,32)
            y = random.randrange(1,24)
            applePosition = [int(x)*20,int(y)*20]
            appleleft = 1

        playSurface.fill(black)
        for position in snakeSegments:
            pygame.draw.rect(playSurface,white,Rect(position[0],position[1],20,20))
            pygame.draw.rect(playSurface,red,Rect(applePosition[0], applePosition[1],20,20))


        pygame.display.flip()

        if snakePosition[0] > 620 or snakePosition[0] < 0:
            gameOver(playSurface)
        if snakePosition[1] > 460 or snakePosition[1] < 0:
            for snakeBody in snakeSegments[1:]:
                if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
                    gameOver(playSurface)

        fps.tick(10)

if __name__ == "__main__":
    main()