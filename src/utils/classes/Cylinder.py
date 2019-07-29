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

        self.rotation = np.array(rotation)
        self.pos = np.array(pos)
        self.height = height
        self.radius = radius
        self.color = color
        self.mass = mass

        self.slices = 50
        self.stacks = 50

    def render(self):

        glLoadIdentity()
        
        glPushMatrix()
        glTranslatef(*self.pos)

        glRotate(self.rotation[0], 1., 0., 0.)
        glRotate(self.rotation[1], 0., 1., 0.)
        glRotate(self.rotation[2], 0., 0., 1.)

        glColor3f(*self.color)
        glutSolidCylinder(self.radius, self.height, self.slices, self.stacks)

        glPopMatrix()
