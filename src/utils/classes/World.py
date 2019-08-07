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
from utils.constants import WINDOW_SIZE

# Class
# ----------------------------------------------------------------------------

class World:

    def __init__(self, window_size=WINDOW_SIZE, clear_color=WHITE4F):

        self.width, self.height = window_size
        self.clear_color = clear_color

        self.objects = []
        self.perspective = (60., self.width / self.height, .1, 100.)

    def init_scene(self):

        glutInit(sys.argv)
        glClearColor(*self.clear_color)
        glEnable(GL_DEPTH_TEST)
        glClearDepth(1.)
        glDepthFunc(GL_LESS)
        glShadeModel(GL_SMOOTH)

        self._set_view()

    def add_object(self, obj):
    
        self.objects.append(obj)

    def render(self):

        for obj in self.objects:
            obj.render()

    def clear(self):

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    def _set_view(self):

        gluPerspective(*self.perspective)
        glTranslatef(0., 0., -10.)





