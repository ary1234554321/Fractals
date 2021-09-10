import sys
import random
import pygame
from pygame.locals import *
import math
from pygame import gfxdraw
from copy import deepcopy
#sv = input("Starting Vector: ")
#co = input("cords: ")

#co = co.split(" ")
#x= int(co[0])
#y= int(co[1])
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

def drawtriangle(p0,p1,p2):
    pygame.draw.polygon(surface=screen, color=(0, 0, 0), points=[(p0[0], p0[1]), (p1[0], p1[1]),(p2[0], p2[1])])
angle = 45
limit = 8
def sier(p0,p1,p2,limit):
    if limit > 0:
        pA = [0,0]
        pA[0] = (p0[0] + p1[0]) /2
        pA[1] = (p0[1] + p1[1]) /2
        pB = [0,0]
        pB[0] = (p1[0] + p2[0]) /2
        pB[1] = (p1[1] + p2[1]) /2
        pC = [0,0]
        pC[0] = (p2[0] + p0[0]) /2
        pC[1] = (p2[1] + p0[1]) /2

        sier(p0,pA,pC,limit-1)
        sier(pA,p1,pB,limit-1)
        sier(pC,pB,p2,limit-1)
    else:
        drawtriangle(p0,p1,p2)
points1 = [[900,0],[900,900],[350,620]]
points2 = [[900,0],[900,900],[1450,620]]

flx = True
fly = True
while True:
    xcord, ycord = pygame.mouse.get_pos()
    backg1()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # if flx:
    #     points[0][0] += 5
    # else:
    #     points[0][0] -= 5
    #
    # if points[0][0] >= 1800:
    #     flx = False
    # if points[0][0] <= 0:
    #     flx = True



    # if fly:
    #     points[0][1] += 5
    # else:
    #     points[0][1] -= 5
    #
    # if points[0][1] <= 100:
    #     fly = True
    # if points[0][1] >= 400:
    #     fly = False

    sier(points2[0],points2[1],points2[2],limit)

    sier(points1[0],points1[1],points1[2],limit)
    fpsClock.tick(60)
    pygame.display.update()