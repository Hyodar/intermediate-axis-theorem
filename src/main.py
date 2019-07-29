#!/usr/bin/python

# Intermediate Axis Theorem Simulator
# Author: Franco Barpp Gomes (https://github.com/Hyodar)

# -*- coding: utf-8 -*-

# Imported modules
# ----------------------------------------------------------------------------

import pygame.locals as pyg
import pygame

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from utils.constants import WINDOW_POSITION
from utils.constants import WINDOW_TITLE
from utils.constants import WINDOW_SIZE

from utils.classes.Cylinder import Cylinder
from utils.classes.World import World

# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------


def main():

    pygame.init()
    pygame.display.set_mode(WINDOW_SIZE, pyg.DOUBLEBUF | pyg.OPENGL)

    world = World(WINDOW_SIZE, WINDOW_POSITION, WINDOW_TITLE)
    world.init_scene()

    cylinder = Cylinder(rotation=(0., 0., 0.),
                        pos=(0., 0., 0.),
                        radius=.5,
                        height=2)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

        cylinder.render()
        #world.process()
        #world.render()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':
    main()