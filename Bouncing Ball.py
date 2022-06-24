# Program for Bouncing Ball
import sys
import pygame

pygame.init()
size=width, height=1300, 700
speed=[1,1]
background=0, 255, 0
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing ball")
ball = pygame.image.load("ball2.png")
ballrect=ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: sys.exit()
    ballrect=ballrect.move(speed)

    if ballrect.left<0 or ballrect.right>width:
        speed[0]=-speed[0]

    if ballrect.top<0 or ballrect.bottom>height:
        speed[1]=-speed[1]
    screen.fill(background)

    screen.blit(ball,ballrect)
    pygame.display.flip()
