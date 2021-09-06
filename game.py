import pygame
pygame.init()#ініцілізація пайгейм
win = pygame.display.set_mode((500,550))#розмір вікна

pygame.display.set_caption('My_Game')
walkRight = [pygame.image.load('right_1.png'), pygame.image.load('right_2.png'),
             pygame.image.load('right_3.png'), pygame.image.load('right_4.png'),
             pygame.image.load('right_5.png'),pygame.image.load('right_6.png')]

walkLeft = [pygame.image.load('left_1.png'), pygame.image.load('left_2.png'),
            pygame.image.load('left_3.png'), pygame.image.load('left_4.png'),
            pygame.image.load('left_5.png'), pygame.image.load('left_6.png')]

bg = pygame.image.load('fon.jpg')
playerStand = pygame.image.load('up.png')

x = 30
y = 454
widht = 80
height = 95
speed = 7

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0
lastMove = 'right'
clock = pygame.time.Clock()

run = True
bulltes = []

class snaryad():
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8*facing
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)



def Window():
    global animCount
    win.blit(bg,(0,0))

    if animCount +1>= 30:
        animCount = 0

    if left :
        win.blit(walkLeft[animCount//5],(x,y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount//5],(x,y))
        animCount += 1
    else:
        win.blit(playerStand,(x,y))
    pygame.display.update()

    for bullte in bulltes:
        bullte.draw(win)
    pygame.display.update()

while run:
    Window()

    clock.tick(30)
    # pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullte in bulltes:
        if bullte.x<500 and bullte.x > 0:
            bullte.x += bullte.vel
        else:
            bulltes.pop(bulltes.index(bullte))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        if lastMove =='right':
            facing = 1
        else:
            facing  = -1
        if len(bulltes)<3:
            bulltes.append(snaryad(round(x+widht//2),round(y+height//2),5,(255,0,0),facing ))


    if keys[pygame.K_LEFT]and x>-5:
        x -= speed
        left = True
        right = False
        lastMove = 'left'
    elif keys[pygame.K_RIGHT]and x<450-15:
        x += speed
        left = False
        right = True
        lastMove = 'right'
    else:
        left = False
        right = False
        animCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True

    else:
        if jumpCount >= -10:#прижок
            if jumpCount < 0:
                y += (jumpCount ** 2) / 3
            else:
                y -= (jumpCount**2)/3
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10


pygame.quit()
