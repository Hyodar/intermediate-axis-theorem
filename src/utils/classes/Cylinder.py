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

    def __init__(self, pos, rotation, height, radius):

        self.pos = pos.copy()
        self.rotation = rotation.copy()
        self.height = height
        self.radius = radius

        self.slices = 20
        self.stacks = 20

        self._create_quad()

    def _create_quad(self):

        self.quad = gluNewQuadric()
        gluQuadricNormals(self.quadric, GLU_SMOOTH)
        gluQuadricTexture(self.quadric, GLU_FALSE)

    def render(self):

        glPushMatrix()
        glTranslatef(*self.pos)

        glRotate(self.rotation[0], 1., 0., 0.)
        glRotate(self.rotation[1], 0., 1., 0.)
        glRotate(self.rotation[2], 0., 0., 1.)

        glutSolidCylinder(height=self.height,
                          slices=self.slices,
                          stacks=self.stacks,
                          base=self.radius,
                          top=self.radius,
                          quad=self.quad)
        glPopMatrix()
