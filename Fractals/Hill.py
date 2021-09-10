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

lim = 8
p0 = [0,800]
p1 = [1800,800]
from numba import jit


@jit(nopython=True)

def hill(p0,p4,limit):
    dx = p4[0] - p0[0]
    dy = p4[1] - p0[1]
    size = math.sqrt(dx**2 + dy **2)

    p1 = [p0[0] + dx * 0.25, p0[1] + dy * 0.25]
    p3 = [p0[0] + dx * 0.75, p0[1] + dy * 0.75]


    ang = -1 * math.degrees(math.atan2(p3[1] - p1[1],p3[0] - p1[0]))
    ta = ang + anglea

    pp5 = [p0[0] + dx * 0.5, p0[1] + dy * 0.5]
    d1x = pp5[0] - p1[0]
    d1y = pp5[1] - p1[1]

    d2 = math.sqrt(d1x **2 + d1y **2)
    le = d2/math.cos(math.radians(anglea))
    p2 = [p1[0] + le * math.cos(math.radians(ta)) ,p1[1] - le * math.sin(math.radians(ta)) ]


    if limit > 0:
        hill(p0,p1,limit - 1)
        hill(p1,p2,limit - 1)
        hill(p2,p3,limit - 1)
        hill(p3,p4,limit - 1)
    else:
        pygame.draw.line(screen, black, (p0[0],p0[1]), (p1[0],p1[1]), 2)
        pygame.draw.line(screen, black, (p1[0],p1[1]), (p2[0],p2[1]), 2)
        pygame.draw.line(screen, black, (p2[0],p2[1]), (p3[0],p3[1]), 2)
        pygame.draw.line(screen, black, (p3[0],p3[1]), (p4[0],p4[1]), 2)


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
    anglea = (xcord/1800) * 360
    hill(p0,p1,lim)
    fpsClock.tick(30)
    pygame.display.update()

