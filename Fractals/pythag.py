import sys
import random
import pygame
from pygame.locals import *
import math
from pygame import gfxdraw
from copy import deepcopy

x = 200
y = 200
white = (255,255,255)
green = (165,238,93)
pink = (245,212,229)
red = (230,69,83)
blue = (85,75,230)
black = (0,0,0)
grey = (130,130,130)
pygame.init()
width, height = 1800,900
screen = pygame.display.set_mode((width,height))

#300 150
pygame.display.set_caption('ptree')

fpsClock = pygame.time.Clock()

def backg1():
    screen.fill(white)

anglea = 45
angleb = 90-anglea
lim = 10
p0 = [900,800]
p1 = [900,600]
def atan(y,x):
    if x != 0:
        t = math.atan(y/x)
        return t

    if x == 0:
        return 0



def pt2(p0,p1,limit):
    dx = p1[0] - p0[0]
    dy = p1[1] - p0[1]
    pE = [p0[0] - dy,p0[1] + dx]
    pD = [p1[0] - dy,p1[1] + dx]
    size = math.sqrt(dx ** 2 + dy ** 2)
    #RIGHT:
    rl = math.cos(math.radians(anglea)) * size

    otangle = math.degrees(math.atan2(pD[0] - p1[0],pD[1] - p1[1])) - 90
    rangle = 90 - anglea - otangle
    print(rangle)


    pA = [p1[0] + (-1 * math.cos(math.radians(rangle) )* rl)  ,p1[1]  - math.sin(math.radians(rangle)) * rl]

    dAx = p1[0] - pA[0]
    dAy = p1[1] - pA[1]


    pB = [pA[0] + dAy,pA[1] - dAx]
    p2 = [p1[0] + dAy, p1[1] - dAx]



    #LEFT

    d2x = pD[0] - p2[0]
    d2y = pD[1] - p2[1]

    pF = [pD[0] + d2y,pD[1] - d2x]

    pC = [p2[0] + d2y, p2[1] - d2x]
    # pygame.draw.circle(screen, black, (pC[0],pC[1]), 10)
    #
    # pygame.draw.circle(screen, black, (pB[0],pB[1]), 10)
    # pygame.draw.circle(screen, pink, (p2[0],p2[1]), 10)
    # pygame.draw.circle(screen, green, (pF[0],pF[1]), 10)
    #
    # pygame.draw.circle(screen, pink, (p0[0],p0[1]), 10)
    # pygame.draw.circle(screen, red, (p1[0],p1[1]), 10)
    # pygame.draw.circle(screen, blue, (pE[0],pE[1]), 10)
    # pygame.draw.circle(screen, pink, (pA[0],pA[1]), 10)
    # pygame.draw.circle(screen, black, (pD[0],pD[1]), 10)

    pygame.draw.polygon(screen, black, points=[(p0[0], p0[1]), (p1[0], p1[1]), (pD[0], pD[1]), (pE[0], pE[1])])


    if limit > 0:
        pt2(p1,pA,limit -1)
        pt2(p2, pC, limit - 1)
    else:
        pygame.draw.polygon(screen, black, points=[(p1[0], p1[1]), (pA[0], pA[1]), (pB[0], pB[1]), (p2[0], p2[1])])
        pygame.draw.polygon(screen, black, points=[(p2[0], p2[1]), (pC[0], pC[1]), (pF[0], pF[1]), (pD[0], pD[1])])
flx = True


while True:
    xcord, ycord = pygame.mouse.get_pos()
    backg1()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                p0[0] += 10
            if event.button == 3:
                p0[0] -= 10

    anglea = (xcord/1800) * 90
    pt2(p0,p1,lim)
    fpsClock.tick(30)
    pygame.display.update()

