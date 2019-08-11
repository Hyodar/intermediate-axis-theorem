#!/usr/bin/env python

# Intermediate Axis Theorem Simulator -> Cylinder
# Author: Franco Barpp Gomes (https://github.com/Hyodar)

# -*- coding: utf-8 -*-

# Imported modules
# ----------------------------------------------------------------------------

import numpy as np

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
        self.x = np.array((3, 0, 0))
        self.y = np.array((0, 3, 0))
        self.z = np.array((0, 0, 3))

    """
    Axes._draw_line(vector:np.array, color:tuple)
        draws a vector from its position
    """

    def _draw_line(self, vector, color):

        glColor(color)
        glBegin(GL_LINES)
        glVertex(self.pos)
        glVertex(self.pos + vector)
        glEnd()

    """
    Axes.render([pos:tuple])
        renders the x, y and z axes
    """

    def render(self, pos=(0, 0, 0)):
     
        glPushMatrix()

        self.pos = np.array(pos, dtype=np.float)

        glLineWidth(2)
        self._draw_line(self.x, YELLOW3F)
        self._draw_line(self.y, GREEN3F)
        self._draw_line(self.z, BLUE3F)
        glLineWidth(1)
        glPopMatrix()
