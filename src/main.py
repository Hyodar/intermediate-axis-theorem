#!/usr/bin/python

# Intermediate Axis Theorem Simulator
# Author: Franco Barpp Gomes (https://github.com/Hyodar)

# -*- coding: utf-8 -*-

# Imported modules
# ----------------------------------------------------------------------------

import pygame.locals as pygl
import pygame

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from utils.constants import WINDOW_POSITION
from utils.constants import WINDOW_TITLE
from utils.constants import WINDOW_SIZE

from utils.classes.Cylinder import Cylinder
from utils.classes.World import World
from utils.classes.Tbar import Tbar

# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

"""
vertices= (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
    
"""

def main():

    pygame.init()
    pygame.display.set_mode(WINDOW_SIZE, pygl.DOUBLEBUF | pygl.OPENGL)

    world = World(WINDOW_SIZE, WINDOW_POSITION, WINDOW_TITLE)
    world.init_scene()

    tbar = Tbar(size=1, rotation=(0., 0., 0.), pos=(0., 0., 0.), angvel=(100, .1, .1))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

        world.clear()

        tbar.render()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':
    main()
