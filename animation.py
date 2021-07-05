import pygame

pygame.init()

walking_right= [pygame.image.load('assets/walking/walk00.png'), pygame.image.load('assets/walking/walk01.png'),
                pygame.image.load('assets/walking/walk02.png'), pygame.image.load('assets/walking/walk03.png'),
                pygame.image.load('assets/walking/walk04.png'), pygame.image.load('assets/walking/walk05.png'),
                pygame.image.load('assets/walking/walk06.png'), pygame.image.load('assets/walking/walk07.png'),
                pygame.image.load('assets/walking/walk08.png'), pygame.image.load('assets/walking/walk09.png')]

walking_left = [pygame.image.load('assets/walking/walkl00.png'), pygame.image.load('assets/walking/walkl01.png'),
                pygame.image.load('assets/walking/walkl02.png'), pygame.image.load('assets/walking/walkl03.png'),
                pygame.image.load('assets/walking/walkl04.png'), pygame.image.load('assets/walking/walkl05.png'),
                pygame.image.load('assets/walking/walkl06.png'), pygame.image.load('assets/walking/walkl07.png'),
                pygame.image.load('assets/walking/walkl08.png'), pygame.image.load('assets/walking/walkl09.png'),]

bg = pygame.image.load('assets/background.png')
# char = pygame.image.load('')
standing_right = [pygame.image.load('assets/standing/stand0.png'), pygame.image.load('assets/standing/stand1.png'),
                  pygame.image.load('assets/standing/stand2.png'), pygame.image.load('assets/standing/stand3.png'),
                  pygame.image.load('assets/standing/stand4.png'), pygame.image.load('assets/standing/stand5.png'),
                  pygame.image.load('assets/standing/stand6.png'), pygame.image.load('assets/standing/stand7.png'),]

standing_left = [pygame.image.load('assets/standing/standl0.png'), pygame.image.load('assets/standing/standl1.png'),
                 pygame.image.load('assets/standing/standl2.png'), pygame.image.load('assets/standing/standl3.png'),
                 pygame.image.load('assets/standing/standl4.png'), pygame.image.load('assets/standing/standl5.png'),
                 pygame.image.load('assets/standing/standl6.png'), pygame.image.load('assets/standing/standl7.png'),]

x = 20
y = 220
width = 1
height = 120


isJump = False
jumpCount = 10

jumping_right = [pygame.image.load('assets/jumping/jump0.png'),pygame.image.load('assets/jumping/jump1.png'),
                 pygame.image.load('assets/jumping/jump2.png'),pygame.image.load('assets/jumping/jump3.png'),
                 pygame.image.load('assets/falling/fall0.png'),pygame.image.load('assets/falling/fall1.png'),
                  pygame.image.load('assets/falling/fall2.png'),pygame.image.load('assets/falling/fall3.png'),]

jumping_left = [pygame.image.load('assets/jumping/jumpl0.png'),pygame.image.load('assets/jumping/jumpl1.png'),
                pygame.image.load('assets/jumping/jumpl2.png'),pygame.image.load('assets/jumping/jumpl3.png'),
                pygame.image.load('assets/falling/falll0.png'),pygame.image.load('assets/falling/falll1.png'),
                  pygame.image.load('assets/falling/falll2.png'),pygame.image.load('assets/falling/falll3.png'),]

run_right = [pygame.image.load('assets/running/run0.png'),pygame.image.load('assets/running/run1.png'),
            pygame.image.load('assets/running/run2.png'),pygame.image.load('assets/running/run3.png'),
            pygame.image.load('assets/running/run4.png'),pygame.image.load('assets/running/run5.png'),
            pygame.image.load('assets/running/run6.png'),pygame.image.load('assets/running/run7.png'),
            pygame.image.load('assets/running/run8.png')]

run_left = [pygame.image.load('assets/running/runl0.png'),pygame.image.load('assets/running/runl1.png'),
            pygame.image.load('assets/running/runl2.png'),pygame.image.load('assets/running/runl3.png'),
            pygame.image.load('assets/running/runl4.png'),pygame.image.load('assets/running/runl5.png'),
            pygame.image.load('assets/running/runl6.png'),pygame.image.load('assets/running/runl7.png'),
            pygame.image.load('assets/running/runl8.png')]

vel = 12
currentvel = 0

screen = pygame.display.set_mode((800, 500))

clock = pygame.time.Clock()

left = False
right = True
rightjump = False
leftjump = False

walkCount = 0


def redrawGameWindow():
    global walkCount
    screen.blit(bg, (0, 0))

    # standing mario
    if currentvel == 0:
        if right:
            if isJump:
                if walkCount//3 >= len(jumping_right):
                    walkCount = 0
                screen.blit(jumping_right[walkCount // 3], (x, y))
                walkCount += 1
            else:
                if walkCount//3 >= len(standing_right):
                    walkCount = 0
                screen.blit(standing_right[walkCount//3], (x, y))
                walkCount += 1
        if left:
            if isJump:
                if walkCount//3 >= len(jumping_left):
                    walkCount = 0
                screen.blit(jumping_left[walkCount // 3], (x, y))
                walkCount += 1
            else:
                if walkCount//3 >= len(standing_left):
                    walkCount = 0
                screen.blit(standing_left[walkCount//3], (x, y))
                walkCount += 1

    elif walkCount + 1 >= 27 and not isJump:
        walkCount = 0

    # mario walking left
    elif left:
        if not isJump:
            if vel == 24:
                if walkCount//3 >= len(run_left):
                    walkCount = 0
                screen.blit(run_left[walkCount//3], (x, y))
                walkCount += 1
            else:
                if walkCount//3 >= len(walking_left):
                    walkCount = 0
                screen.blit(walking_left[walkCount//3], (x, y))
                walkCount += 1
        else:
            if walkCount//3 >= len(jumping_left):
                walkCount = 0
            screen.blit(jumping_left[walkCount // 3], (x, y))
            walkCount += 1

    # mario walking right
    elif right:
        if not isJump:
            if vel == 24:
                if walkCount//3 >= len(run_right):
                    walkCount = 0
                screen.blit(run_right[walkCount//3], (x, y))
                walkCount += 1
            else:
                if walkCount//3 >= len(walking_right):
                    walkCount = 0
                screen.blit(walking_right[walkCount // 3], (x, y))
                walkCount += 1
        else:
            if walkCount//3 >= len(jumping_right):
                walkCount = 0
            screen.blit(jumping_right[walkCount // 3], (x, y))
            walkCount += 1

    pygame.display.update()


run = True

while run:
    x += currentvel
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        currentvel = -vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT]:
        currentvel = vel
        left = False
        right = True

    elif keys[pygame.K_LSHIFT]:
        vel = 24

    else:
        currentvel = 0
        vel = 12

    if not (isJump):
        if keys[pygame.K_SPACE] and keys[pygame.K_RIGHT]:
            isJump = True
            leftjump = False
            rightjump = True
            walkCount = 0

        if keys[pygame.K_SPACE] and keys[pygame.K_LEFT]:
            isJump = True
            rightjump = False
            leftjump = True
            walkCount = 0
        
        if keys[pygame.K_SPACE]:
            isJump = True
            walkCount = 0
                
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    redrawGameWindow()
pygame.quit()
