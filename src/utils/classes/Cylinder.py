#!/usr/bin/python

# Intermediate Axis Theorem Simulator -> Cylinder
# Author: Franco Barpp Gomes (https://github.com/Hyodar)

# -*- coding: utf-8 -*-

# Imported modules
# ----------------------------------------------------------------------------

import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from utils.constants import DEFAULT_DELAY
from utils.classes.Axes import Axes


# Class
# ----------------------------------------------------------------------------


class Cylinder:

    def __init__(self, pos, rotation, color, height, radius, mass):

        self.rotation = np.array(rotation, dtype=np.float)
        self.pos = np.array(pos, dtype=np.float)
        self.height = height
        self.radius = radius
        self.color = color
        self.mass = mass

        self.slices = 10
        self.stacks = 1

    """
    Cylinder.render(tbar_cm:tuple, rel_pos:tuple)
        renders the cylinder based on the tbar's center of mass 
        and the relative position
    """

    def render(self, tbar_cm, rel_pos):

        glPushMatrix()
        glTranslate(*tbar_cm)
        glTranslate(*rel_pos)

        glRotatef(self.rotation[0], 1, 0, 0)
        glRotatef(self.rotation[1], 0, 1, 0)
        glRotatef(self.rotation[2], 0, 0, 1)

        glColor3f(*self.color)
        glutWireCylinder(self.radius, self.height, self.slices, self.stacks)

        glPopMatrix()

