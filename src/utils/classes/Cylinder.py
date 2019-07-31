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

        self.slices = 50
        self.stacks = 50

    def render(self, tbar_angle, tbar_cm, tbar_pos, rel_pos):

        glPushMatrix()
        glTranslate(*tbar_pos)
        
        glRotatef(tbar_angle[0], 1, 0, 0)
        glRotatef(tbar_angle[1], 0, 1, 0)
        glRotatef(tbar_angle[2], 0, 0, 1)

        glTranslate(*rel_pos)

        glRotatef(self.rotation[0], 1, 0, 0)
        glRotatef(self.rotation[1], 0, 1, 0)
        glRotatef(self.rotation[2], 0, 0, 1)

        glColor3f(*self.color)
        glutWireCylinder(self.radius, self.height, self.slices, self.stacks)

        glPopMatrix()
