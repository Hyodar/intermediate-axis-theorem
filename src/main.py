#!/usr/bin/env python

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

from utils.constants import WINDOW_SIZE
from utils.constants import NUM_FRAMES

from utils.classes.Screen import Screen
from utils.classes.World import World
from utils.classes.Tbar import Tbar

# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------


def main():

    print('[*] Creating pygame display...')
    pygame.init()
    display = pygame.display.set_mode(WINDOW_SIZE, pygl.DOUBLEBUF | pygl.OPENGL)

    world = World()
    tbar = Tbar()
    world.add_object(tbar)

    screen = Screen(display=display, tbar=tbar)

    print('[*] Initializing scene...')
    world.init_scene()

    frame = 0
    paused = False

    print('[*] Starting pygame loop...')
    while frame < NUM_FRAMES:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('[*] Quit event detected. Stopping pygame...')
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                    if paused:
                        screen.show_paused_message()

        if not paused:
            world.clear()
            world.render()
            screen.render()

            frame += 1

            pygame.display.flip()
            pygame.time.wait(10)

    print('[*] Simulation finished successfully')


if __name__ == '__main__':
    main()
