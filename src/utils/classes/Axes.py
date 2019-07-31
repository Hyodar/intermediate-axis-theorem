#!/usr/bin/python

# Intermediate Axis Theorem Simulator -> Cylinder
# Author: Franco Barpp Gomes (https://github.com/Hyodar)

# -*- coding: utf-8 -*-

# Imported modules
# ----------------------------------------------------------------------------

import numpy as np
import pygame as pyg

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from utils.constants import GREEN3F
from utils.constants import BLUE3F
from utils.constants import YELLOW3F

# Class
# ----------------------------------------------------------------------------


class Axes:

    def __init__(self, pos):

        self.pos = np.array(pos, dtype=np.float)

    def _draw_line(self, vector, color):

        glColor(color)
        glBegin(GL_LINES)
        glVertex(self.pos)
        glVertex(self.pos + vector)
        glEnd()

    def render(self, rotation=(0,0,0), pos=(-2, 0, 0)):
     
        glPushMatrix()

        self.pos = np.array(pos, dtype=np.float)

        glRotatef(rotation[0], 1, 0, 0)
        glRotatef(rotation[1], 0, 1, 0)
        glRotatef(rotation[2], 0, 0, 1)

        self._draw_line(np.array((3., 0., 0.)), YELLOW3F)
        self._draw_line(np.array((0., 3., 0.)), GREEN3F)
        self._draw_line(np.array((0., 0., 3.)), BLUE3F)

        glPopMatrix()
