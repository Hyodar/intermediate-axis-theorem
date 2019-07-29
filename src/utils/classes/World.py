#!/usr/bin/python

# Intermediate Axis Theorem Simulator -> World
# Author: Franco Barpp Gomes (https://github.com/Hyodar)

# -*- coding: utf-8 -*-

# Imported modules
# ----------------------------------------------------------------------------

import sys

import numpy as np
import pygame as pyg

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from utils.constants import WHITE
from utils.constants import WINDOW_TITLE

# Class
# ----------------------------------------------------------------------------

class World:

    def __init__(self, window_size, window_position, window_title):

        self.width, self.height = window_size
        self.pos = window_position
        self.title = window_title

        self.perspective = [45., self.width / self.height, .1, 100.]

    def init_scene(self):

        glClearColor(*WHITE)
        glClearDepth(1.)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)

        self._set_view()
        self._set_lighting()

    def init_window(self):

        glutInit(sys.argv)

        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(self.height, self.width)
        glutInitWindowPosition(*self.pos)

        self.window = glutCreateWindow(self.title)

    def _set_view(self):

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        gluPerspective(*self.perspective)

        glMatrixMode(GL_MODELVIEW)

    def _set_lighting(self):

        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.5, 0.5, 0.5, 1.0))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))
        glLightfv(GL_LIGHT0, GL_POSITION, (0.0, 0.0, 2.0, 1.0))
        glEnable(GL_LIGHT0)




