#!/usr/bin/env python

# Intermediate Axis Theorem Simulator -> World
# Author: Franco Barpp Gomes (https://github.com/Hyodar)

# -*- coding: utf-8 -*-

# Imported modules
# ----------------------------------------------------------------------------

import sys

import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *

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

    """
    World.init_scene()
        sets some parameters on opengl
    """

    def init_scene(self):

        glClearColor(*self.clear_color)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        glClearDepth(1.)
        glDepthFunc(GL_LESS)
        glShadeModel(GL_SMOOTH)

        gluPerspective(*self.perspective)
        glTranslatef(0., 0., -10.)

    """
    World.add_object(obj:any)
        adds an object to the rendering list
    """

    def add_object(self, obj):    
        self.objects.append(obj)

    """
    World.step()
        steps all the objects on the rendering list
    """

    def step(self):
        for obj in self.objects:
            obj.step()

    """
    World.render()
        renders all the objects on the rendering list
    """

    def render(self):
        for obj in self.objects:
            obj.render()

    """
    World.clear()
        clears the color and depth buffer
    """

    def clear(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)



