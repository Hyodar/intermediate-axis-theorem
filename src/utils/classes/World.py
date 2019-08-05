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

from utils.constants import WHITE4F
from utils.constants import WINDOW_TITLE

# Class
# ----------------------------------------------------------------------------

class World:

    def __init__(self, window_size, window_position, window_title):

        self.width, self.height = window_size
        self.pos = window_position
        self.title = window_title

        self.perspective = [60., self.width / self.height, .1, 100.]

    def init_scene(self):

        glutInit(sys.argv)
        glClearColor(*WHITE4F)
        glEnable(GL_DEPTH_TEST)
        glClearDepth(1.)
        glDepthFunc(GL_LESS)
        glShadeModel(GL_SMOOTH)

        self._set_view()
        #self._set_lighting()

    def clear(self):

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    def _set_view(self):

        gluPerspective(*self.perspective)
        glTranslatef(0., 0., -10.)

    def _set_lighting(self):

        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.5, 0.5, 0.5, 1.0))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))
        glLightfv(GL_LIGHT0, GL_POSITION, (0.0, 0.0, 2.0, 1.0))
        glEnable(GL_LIGHT0)




