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

from utils.constants import DEFAULT_DELAY

from utils.classes.Cylinder import Cylinder
from utils.classes.World import World
from utils.classes.Axes import Axes
from utils.classes.Tbar import Tbar

# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------


def main():

    pygame.init()
    pygame.display.set_mode(WINDOW_SIZE, pygl.DOUBLEBUF | pygl.OPENGL)

    world = World(WINDOW_SIZE, WINDOW_POSITION, WINDOW_TITLE)
    world.init_scene()

    tbar = Tbar(size=3, rotation=(0., 0., 0.), pos=(0., 0., 0.), angvel=(4, .1, .1))
    axes = Axes(pos=(-4., 0., 0.))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

        world.clear()

        tbar.render()
        axes.render()

        #exit(0)

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':
    main()
