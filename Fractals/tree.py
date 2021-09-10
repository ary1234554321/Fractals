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
pygame.display.set_caption('Phylo')

fpsClock = pygame.time.Clock()
def backg1():
    screen.fill(white)

p0 = [900,800]
p1 = [900,200]
branchangle1 = random.randint(1,360)
branchangle2 = random.randint(1,360)
tr = 0.4
lim = 12

def tree(p0,p1,limit):
    dx = p1[0] - p0[0]
    dy = p1[1] - p0[1]
    dist = math.sqrt(dx**2 + dy**2)

    angle = math.atan2(dy,dx)


    brl = dist * (1-tr)

    pA = [p0[0] + dx * tr,p0[1] + dy*tr]
    pB = [pA[0] + math.cos(angle + math.radians(branchangle1)) * brl ,pA[1] + math.sin(angle + math.radians(branchangle1)) * brl]
    pC = [pA[0] + math.cos(angle - math.radians(branchangle2)) * brl ,pA[1] + math.sin(angle - math.radians(branchangle2)) * brl]

    pygame.draw.line(screen, black , (p0[0],p0[1]) , (pA[0],pA[1]) ,width=2)

    if limit > 0:
        tree(pA,pB,limit-1)
        tree(pA,pC,limit-1)
    else:
        pygame.draw.line(screen, black, (pA[0], pA[1]), (pB[0], pB[1]),width=2 )

        pygame.draw.line(screen, black, (pA[0], pA[1]), (pC[0], pC[1]),width=2 )
flx = True
fly = True

while True:
    xcord, ycord = pygame.mouse.get_pos()
    backg1()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                branchangle1 = random.randint(1, 360)
                branchangle2 = random.randint(1, 360)

    if flx:
        branchangle1 += 1
    else:
        branchangle1 -= 1

    if branchangle1 <= 1:
        flx = True
    if branchangle1 >= 89:
        flx = False


    if fly:
        branchangle2 -= 1.5
    else:
        branchangle2 -= 1

    if branchangle2 <= 1:
        fly = True
    if branchangle2 >= 89:
        fly = False

    tree(p0,p1,lim)
    fpsClock.tick(30)
    pygame.display.update()