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

    def __init__(self, pos, rotation, color, height, radius):

        self.rotation = rotation
        self.height = height
        self.radius = radius
        self.color = color
        self.pos = pos

        self.slices = 50
        self.stacks = 50

        self._create_quad()

    def _create_quad(self):

        self.quad = gluNewQuadric()
        gluQuadricNormals(self.quad, GLU_SMOOTH)
        gluQuadricTexture(self.quad, GLU_FALSE)

    def render(self):

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
        glPushMatrix()
        glTranslatef(*self.pos)

        glRotate(self.rotation[0], 1., 0., 0.)
        glRotate(self.rotation[1], 0., 1., 0.)
        glRotate(self.rotation[2], 0., 0., 1.)

        glColor3f(*self.color)
        glutSolidCylinder(self.radius, self.height, self.slices, self.stacks)

        glPopMatrix()

